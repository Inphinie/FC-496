# FC-496 Bit Structure Specification
**Version:** 2.1.6 (Unified)
**Total Size:** 496 Bits (62 Bytes)
**Alignment:** 64-Byte (with 16-bit padding for AVX-512)

---

## 1. The Golden Partition ($\varphi$)
The cell is physically divided based on the Golden Ratio to maximize entropic efficiency.

| Segment | Taille (Bits) | Taille (Bytes) | Fonction |
| :--- | :---: | :---: | :--- |
| **MINOR** (Control) | **190** | ~23.75 | Header, Contexte, Sécurité |
| **MAJOR** (Payload) | **306** | ~38.25 | Contenu Sémantique, Embedding |

*Ratio : $306 / 190 \approx 1.6105$ (Précision $\varphi$ à 99.5%)*

---

## 2. Detailed Memory Map

### 🟦 MINOR SEGMENT (190 Bits) - The "Soul"
*Situé en tête pour le filtrage rapide par le Kernel (H-Scale validation).*

1.  **Magic Signature (16 bits)** : `0x1F0` (Valeur 496).
2.  **$\pi$-Time Index (64 bits)** : Position absolue dans les décimales de $\pi$.
3.  **Geo-Fractal Hash (64 bits)** : Coordonnée spatiale unique.
4.  **Schema Class (16 bits)** : Type de l'atome (ex: 0x01=Text, 0x02=Neuron).
5.  **$\mathcal{H}$-Score (16 bits)** : Métrique d'Harmonie (pour rejet automatique).
6.  **Flags (14 bits)** : Permissions et états (Read-Only, Encrypted...).

**Total : 16 + 64 + 64 + 16 + 16 + 14 = 190 Bits.** ✅

### 🟧 MAJOR SEGMENT (306 Bits) - The "Body"
*Le contenu utile transporté.*

1.  **Semantic Vector / Payload (256 bits)** : Embedding dense ou data compressée (UICT).
2.  **StrandGraph Links (34 bits)** : Pointeurs relatifs (Liaisons chimiques).
3.  **Cyclic Redundancy (16 bits)** : Checksum interne.

**Total : 256 + 34 + 16 = 306 Bits.** ✅

---

## 3. Visual Layout

```text
[MINOR: 190 bits] ................................. [MAJOR: 306 bits]
[Magic|PiTime|Geo|Class|H|Flags] || [Payload (Vector) | Strands | CRC]
