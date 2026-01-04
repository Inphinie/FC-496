# FC-496 : Mathematical Index
**Version:** 2.1
**Scope:** Geometric Partitioning & Validity.

---

## 1. The Partition Equation
Defining the split derived from $\varphi$.

### 📐 LaTeX


$$
S_{major} = \left\lfloor \frac{496}{\varphi} \right\rceil = 306 \text{ bits}
$$


$$
S_{minor} = 496 - S_{major} = 190 \text{ bits}
$$


---

## 2. The Unified State Vector ($\Psi_{cell}$)
A valid cell is a vector combining Payload, Time, and Space, validated by Harmony.

### 📐 LaTeX


$$
\Psi_{cell} = \begin{bmatrix} P_{ayload} \\ T_{\pi} \\ G_{eo} \end{bmatrix} \cdot \delta(\mathcal{H} \ge \varphi^{-1})
$$


Where $\delta$ is the Dirac delta function ensuring the cell vanishes (is rejected) if Harmony $\mathcal{H}$ is below the threshold $1/\varphi \approx 0.618$.

---

## 3. Python Validity Check
The algorithm used by SynapseΩ.

### 💻 Python
```python
PHI = 1.61803398875
THRESHOLD = 1.0 / PHI

def is_valid_atom(h_score, magic_sig):
    # 1. Structural Integrity
    if magic_sig != 0x1F0: return False
    
    # 2. Harmonic Integrity (The Filter)
    if h_score < THRESHOLD: return False
    
    return True
