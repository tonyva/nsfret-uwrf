
import hashlib
import torch  # Use: apt install python3-torch - 250 MB of dependencies 
              #      or pip install torch
import torch.nn as nn

class HashKVCacheSimulator:
    def __init__(self, block_size=4, num_layers=2, num_heads=4, head_dim=16):
        """
        Simulates an LLM prefix cache using a hash table.
        """
        self.block_size = block_size
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.head_dim = head_dim
        
        # The Hash Table: Maps a text/token prefix hash to its physical (K, V) tensors
        self.cache_store = {} 

    def _hash_tokens(self, token_ids: list) -> str:
        """Generates a cryptographic hash for a unique sequence of tokens."""
        token_string = ",".join(map(str, token_ids))
        return hashlib.sha256(token_string.encode('utf-8')).hexdigest()

    def lookup_and_extract(self, full_tokens: list):
        """
        Scans the input prompt from left to right in 'block_size' steps.
        Returns the longest matched cached tensors and the remaining uncached tokens.
        """
        matched_k = [[] for _ in range(self.num_layers)]
        matched_v = [[] for _ in range(self.num_layers)]
        
        longest_cached_idx = 0
        
        # Traverse tokens by logical blocks
        for i in range(self.block_size, len(full_tokens) + 1, self.block_size):
            sub_sequence = full_tokens[:i]
            seq_hash = self._hash_tokens(sub_sequence)
            
            if seq_hash in self.cache_store:
                longest_cached_idx = i
                # Retrieve the tensors for this specific block
                for layer in range(self.num_layers):
                    matched_k[layer].append(self.cache_store[seq_hash][layer]['k'])
                    matched_v[layer].append(self.cache_store[seq_hash][layer]['v'])
            else:
                break # Cache miss; must compute the rest dynamically

        # Combine block tensors if hits occurred
        if longest_cached_idx > 0:
            final_k = [torch.cat(matched_k[layer], dim=2) for layer in range(self.num_layers)]
            final_v = [torch.cat(matched_v[layer], dim=2) for layer in range(self.num_layers)]
        else:
            final_k, final_v = None, None

        uncached_tokens = full_tokens[longest_cached_idx:]
        return final_k, final_v, uncached_tokens, longest_cached_idx

    def compute_and_save(self, full_tokens: list, start_idx: int, computed_k_layers: list, computed_v_layers: list):
        """
        Takes freshly computed sequence tensors, slices them into block alignments,
        and saves them under their respective sequence hashes into the hash table.
        """
        current_idx = start_idx
        seq_len = computed_k_layers[0].shape[2]  # Sequence dimension from [batch, heads, seq_len, head_dim]
        
        # Calculate how many full blocks can be saved
        while current_idx + self.block_size <= start_idx + seq_len:
            next_boundary = current_idx + self.block_size
            sub_sequence = full_tokens[:next_boundary]
            seq_hash = self._hash_tokens(sub_sequence)
            
            # Extract the specific block slice from the newly processed context
            slice_start = current_idx - start_idx
            slice_end = next_boundary - start_idx
            
            block_data = {}
            for layer in range(self.num_layers):
                block_data[layer] = {
                    'k': computed_k_layers[layer][:, :, slice_start:slice_end, :],
                    'v': computed_v_layers[layer][:, :, slice_start:slice_end, :]
                }
            
            # Commit to the Hash Table
            self.cache_store[seq_hash] = block_data
            current_idx = next_boundary

# --- Simulation Verification ---
if __name__ == "__main__":
    # Mock parameters
    BSize, Layers, Heads, HDim = 4, 2, 4, 16
    simulator = HashKVCacheSimulator(block_size=BSize, num_layers=Layers, num_heads=Heads, head_dim=HDim)
    
    # User Request 1: System Prompt (Length 8 - perfectly fits into 2 blocks)
    prompt_1 = [101, 2003, 1037, 2307, 4392, 1012, 1024, 3000] 
    print(f"Executing Request 1 (Prompt length: {len(prompt_1)})")
    
    # 1. Check Hash Table for Cache Match
    cached_k, cached_v, uncached, match_idx = simulator.lookup_and_extract(prompt_1)
    print(f"Cache hit tokens: {match_idx} | Remaining to compute: {len(uncached)}") 
    
    # 2. Simulate LLM computing KV states for the uncached portion
    # Shape: [Batch=1, Heads=4, Seq_Len=8, Head_Dim=16]
    mock_computed_k = [torch.randn(1, Heads, len(uncached), HDim) for _ in range(Layers)]
    mock_computed_v = [torch.randn(1, Heads, len(uncached), HDim) for _ in range(Layers)]
    
    # 3. Store the new calculations into the hash table
    simulator.compute_and_save(prompt_1, match_idx, mock_computed_k, mock_computed_v)
    print(f"Hash Table Size after Request 1: {len(simulator.cache_store)} blocks cached.\n")
    
    # User Request 2: Shared System Prompt + New Appendage (Total Length: 10)
    prompt_2 = [101, 2003, 1037, 2307, 4392, 1012, 1024, 3000, 9999, 8888]
    print(f"Executing Request 2 (Prompt length: {len(prompt_2)})")
    
    # 1. Lookup using the Hash Table
    cached_k, cached_v, uncached, match_idx = simulator.lookup_and_extract(prompt_2)
    print(f"Cache hit tokens: {match_idx} | Remaining to compute: {len(uncached)}")
    print(f"Retrieved Cached Tensor Shape (Layer 0 K): {cached_k[0].shape}")

