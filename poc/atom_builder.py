"""
FC-496 Atom Builder
Version: 2.1.6 (Unified)
Author: Lichen Collective

Generates a 62-byte (496-bit) atomic cell with:
- Minor Segment (190 bits)
- Major Segment (306 bits)
- Pi-Time Indexing
"""

import struct
import time
import hashlib

# --- CONSTANTS ---
MAGIC_SIG = 0x1F0  # 496
PHI = 1.61803398875
H_THRESHOLD = 1.0 / PHI

class FC496Atom:
    def __init__(self, payload_bytes, pi_index, geo_hash, h_score):
        # --- VALIDATION (Kernel Level) ---
        if h_score < H_THRESHOLD:
            raise ValueError(f"Kernel Panic: H-Score {h_score:.3f} < {H_THRESHOLD:.3f}. Cell Rejected.")
        
        if len(payload_bytes) > 32: # 256 bits = 32 bytes
            # Auto-truncate or hash for demo
            payload_bytes = hashlib.sha256(payload_bytes).digest()

        # --- MINOR SEGMENT (190 bits / ~24 bytes container) ---
        self.magic = MAGIC_SIG       # 16 bits
        self.pi_index = pi_index     # 64 bits
        self.geo_hash = geo_hash     # 64 bits
        self.schema = 0x01           # 16 bits (Text/Data)
        self.h_score = int(h_score * 10000) # 16 bits (Normalized 0-10000)
        self.flags = 0b11110000000000 # 14 bits (Mock)

        # --- MAJOR SEGMENT (306 bits / ~38 bytes container) ---
        self.payload = payload_bytes # 256 bits
        self.strands = 0x0           # 34 bits (Links)
        self.crc = 0xFFFF            # 16 bits

    def serialize(self):
        """
        Packs the atom into a binary stream.
        Note: Python struct alignment makes exact bit-packing tricky.
        This represents the LOGICAL structure.
        """
        # Minor Segment Pack (Using Q=64, H=16)
        # Magic(H), Pi(Q), Geo(Q), Schema(H), H_Score(H), Flags(H - masked)
        minor = struct.pack('>HQQHHH', 
            self.magic, 
            self.pi_index, 
            self.geo_hash, 
            self.schema, 
            self.h_score, 
            self.flags
        )
        
        # Major Segment Pack
        # Payload (32s), Strands (Q - masked), CRC (H)
        major = struct.pack('>32sQH',
            self.payload,
            self.strands,
            self.crc
        )
        
        return minor + major

# --- DEMO ---
if __name__ == "__main__":
    print(f"🌌 FC-496 Atom Builder (Threshold: {H_THRESHOLD:.3f})")
    
    try:
        # Creating a valid cell
        atom = FC496Atom(
            payload_bytes=b"Lichen Universe Manifest V2.1.6",
            pi_index=3141592653,
            geo_hash=0xCAFEBABE,
            h_score=0.95  # High Harmony
        )
        binary_data = atom.serialize()
        print(f"✅ Atom Created! Size: {len(binary_data)} bytes (Target: 62).")
        print(f"Hex Dump: {binary_data.hex().upper()[:64]}...")
        
    except ValueError as e:
        print(f"❌ {e}")
