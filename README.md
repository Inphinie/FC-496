# FC-496 : The Fractal Cell Atom
## L'Unité Fondamentale de l'Univers Lichen

[![Standard](https://img.shields.io/badge/standard-Universal-purple)](specs/bit_structure.md)
[![Size](https://img.shields.io/badge/size-496_bits-blue)](FORMULAS.md)
[![Partition](https://img.shields.io/badge/partition-%CF%86_Split-gold)](FORMULAS.md)
[![License](https://img.shields.io/badge/License-Apache_2.0-grey.svg)](LICENSE)

> **"Data is not a stream. Data is a crystal."**

**FC-496** est une structure de données atomique de taille fixe (**62 bytes** / 496 bits), conçue pour l'efficacité entropique, l'alignement mémoire (SIMD/AVX-512 friendly) et l'indexation native spatio-temporelle.

Contrairement aux formats flexibles (JSON, XML), le FC-496 est une "brique dure" géométriquement parfaite, utilisée par le noyau **SynapseΩ** pour le stockage distribué.

---

## 📐 Architecture Géométrique ($\varphi$)

La cellule est physiquement divisée en deux segments selon la **Partition Dorée** (Golden Ratio) pour maximiser la densité d'information.

| Segment | Rôle | Taille (Bits) | Taille (Bytes) | Ratio |
| :--- | :--- | :---: | :---: | :---: |
| **MINOR** | **Control Plane** (Header, Context, Hash) | **190** | ~23.75 | $1$ |
| **MAJOR** | **Data Plane** (Payload, Vectors) | **306** | ~38.25 | $\varphi$ |
| **TOTAL** | **Atomic Cell** | **496** | **62.00** | $\approx 1.618$ |

> *Note : Avec un padding de 2 bytes (16 bits), la cellule s'aligne parfaitement sur 64 bytes pour le traitement par vecteurs CPU.*

---

## 💾 Memory Map (Bitwise)

### 1. The Minor Segment (L'Âme - 190 bits)
Optimisé pour le filtrage rapide par le Kernel sans décoder le payload.

* `[16]` **Magic Signature** : `0x1F0` (Validation type).
* `[64]` **$\pi$-Time Index** : Position temporelle absolue.
* `[64]` **Geo-Fractal Hash** : Ancrage spatial unique.
* `[16]` **Schema Class** : Type de donnée (Text, Neuron, Audio).
* `[16]` **$\mathcal{H}$-Score** : Métrique d'Harmonie (0-10000).
* `[14]` **Flags** : Permissions et états binaires.

### 2. The Major Segment (Le Corps - 306 bits)
* `[256]` **Semantic Payload** : Vecteur d'embedding ou data brute.
* `[34]`  **StrandGraph Links** : Pointeurs relatifs (Liaisons chimiques).
* `[16]`  **CRC** : Intégrité cyclique.

---

## 🧮 Mathématiques Fondamentales

La validité d'une cellule est définie par l'équation d'état unifié $\Psi_{cell}$. Une cellule n'existe que si son **Score d'Harmonie** ($\mathcal{H}$) dépasse l'inverse de Phi.

$$
\Psi_{cell} = \begin{bmatrix} P_{ayload} \\ T_{\pi} \\ G_{eo} \end{bmatrix} \cdot \delta(\mathcal{H} \ge \varphi^{-1})
$$

Où le seuil de rejet est :
$$\text{Threshold} = \frac{1}{\varphi} \approx 0.618$$

*Voir [FORMULAS.md](FORMULAS.md) pour les démonstrations complètes.*

---

## 💻 Utilisation (Python)

Génération d'un atome valide avec le `atom_builder.py`.

```python
from atom_builder import FC496Atom

# Création d'une cellule
atom = FC496Atom(
    payload_bytes=b"Lichen Universe Manifest V2.1",
    pi_index=3141592653,
    geo_hash=0xCAFEBABE,
    h_score=0.95  # Harmony > 0.618 (Valid)
)

# Sérialisation binaire (62 bytes)
binary_data = atom.serialize()

print(f"Atom Size: {len(binary_data)} bytes")
# Output: Atom Size: 62 bytes
