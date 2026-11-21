import streamlit as st
import random
import time

st.set_page_config(
    page_title="B.Tech All-Branch & Year-Wise AI Study Hub",
    page_icon="🎓",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 55%, #6d28d9 100%);
        padding: 22px;
        border-radius: 16px;
        color: white;
        margin-bottom: 20px;
    }
    .badge-pill {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-block;
        margin-top: 8px;
    }
    .tip-card {
        background-color: #f0f9ff;
        border-left: 5px solid #0284c7;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 12px;
        color: #0f172a;
    }
    .concept-card {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 12px;
        color: #1e293b;
    }
    .viva-card {
        background: linear-gradient(135deg, #fefce8 0%, #fef9c3 100%);
        border: 1px solid #facc15;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: #713f12;
    }
</style>
""", unsafe_allow_html=True)

# Common 1st Year Subjects (Shared across all B.Tech Branches)
FIRST_YEAR_SUBJECTS = {
    "Python & C Programming": {
        "concept": "Control flow (loops, conditionals), functions, arrays, pointers in C, and Python data structures (lists, tuples, dictionaries).",
        "exam_tips": "• Draw neat flowcharts before writing C programs.\n• Dry-run nested loops and pointer arithmetic for 10-mark questions.\n• Always mention Big-O time complexity in searching/sorting answers.",
        "formulas": "Linear Search: O(n) | Binary Search: O(log n) | Bubble Sort: O(n²) | C int size: 4 bytes",
        "viva": [
            ("Difference between `=` and `==`?", "`=` assigns a value, while `==` checks equality between two values."),
            ("Why are Tuples immutable in Python?", "Tuples cannot be changed after creation, making them faster and hashable for dictionary keys.")
        ],
        "questions": [
            {"q": "Which keyword skips the current iteration in a Python loop?", "options": ["break", "continue", "pass", "return"], "ans": "continue", "sol": "`continue` jumps straight to the next iteration of the loop."},
            {"q": "Which operator returns the memory address of a variable in C?", "options": ["*", "&", "->", "#"], "ans": "&", "sol": "`&` is the address-of operator, while `*` dereferences a pointer."},
            {"q": "Which Python collection is immutable?", "options": ["List", "Set", "Dictionary", "Tuple"], "ans": "Tuple", "sol": "Tuples `()` cannot be modified once created."},
            {"q": "Which C loop runs at least once even if the condition is false?", "options": ["for", "while", "do-while", "None"], "ans": "do-while", "sol": "`do-while` evaluates the condition after executing the loop body."},
            {"q": "What is the output of `2 ** 3 ** 2` in Python?", "options": ["64", "512", "18", "12"], "ans": "512", "sol": "Right-associative power: `3**2 = 9`, then `2**9 = 512`."}
        ]
    },
    "Engineering Chemistry": {
        "concept": "Quantum wavefunctions, eigenvalues, UV-Vis electronic transitions (σ, π, n), IR molecular vibrations, and emission spectroscopy.",
        "exam_tips": "• Memorize electronic transition energy order: σ→σ* > n→σ* > π→π* > n→π*.\n• Practice Beer-Lambert Law (A = εcl) numericals.\n• Draw Jablonski diagram for fluorescence vs phosphorescence.",
        "formulas": "Beer-Lambert Law: A = ε · c · l | Photon Energy: E = hν = hc/λ",
        "viva": [
            ("What is a chromophore?", "A covalently unsaturated group (like C=C, C=O) responsible for UV-Vis light absorption."),
            ("Difference between Fluorescence & Phosphorescence?", "Fluorescence is fast (singlet-to-singlet), while phosphorescence has a delayed glow (triplet-to-singlet).")
        ],
        "questions": [
            {"q": "Which EM region causes molecular vibrations?", "options": ["UV-Vis", "Infrared (IR)", "X-Ray", "Microwave"], "ans": "Infrared (IR)", "sol": "IR radiation matches covalent bond stretching and bending frequencies."},
            {"q": "Which transition requires maximum energy?", "options": ["n → π*", "π → π*", "σ → σ*", "n → σ*"], "ans": "σ → σ*", "sol": "Sigma bonds are strongest, requiring highest energy to excite to σ*."},
            {"q": "In A = εcl, 'ε' stands for:", "options": ["Wavelength", "Molar absorptivity", "Path length", "Concentration"], "ans": "Molar absorptivity", "sol": "ε is molar absorptivity (extinction coefficient)."},
            {"q": "An acceptable wavefunction ψ must be:", "options": ["Single-valued & continuous", "Infinite", "Discontinuous", "Zero everywhere"], "ans": "Single-valued & continuous", "sol": "Physical wavefunctions must be finite, single-valued, and continuous."},
            {"q": "Delayed emission from a triplet excited state is called:", "options": ["Fluorescence", "Phosphorescence", "Diffraction", "Refraction"], "ans": "Phosphorescence", "sol": "Phosphorescence occurs via forbidden T1 → S0 transition."}
        ]
    },
    "Engineering Physics & Maths": {
        "concept": "Quantum mechanics (de Broglie, Schrödinger), semiconductor physics, matrices, eigenvalues, and differential calculus.",
        "exam_tips": "• Check eigenvalues using Sum = Trace and Product = Determinant.\n• State boundary conditions clearly in 1D potential box derivations.",
        "formulas": "de Broglie: λ = h/p | Trace(A) = Σλᵢ | Det(A) = Πλᵢ",
        "viva": [
            ("What does |ψ|² represent?", "Probability density of finding a particle at a given position."),
            ("When is a matrix singular?", "When its determinant |A| = 0, meaning its inverse does not exist.")
        ],
        "questions": [
            {"q": "The sum of eigenvalues of a matrix equals its:", "options": ["Determinant", "Rank", "Trace", "Inverse"], "ans": "Trace", "sol": "Sum of main diagonal elements (Trace) equals sum of eigenvalues."},
            {"q": "At 0 K, an intrinsic semiconductor acts as a:", "options": ["Superconductor", "Conductor", "Perfect Insulator", "P-type"], "ans": "Perfect Insulator", "sol": "No thermal energy exists at 0 K to excite valence electrons."},
            {"q": "Which phenomenon proves light is transverse?", "options": ["Interference", "Diffraction", "Polarization", "Reflection"], "ans": "Polarization", "sol": "Only transverse waves can undergo polarization."},
            {"q": "If |A| = 0, matrix A is:", "options": ["Identity", "Singular", "Orthogonal", "Unitary"], "ans": "Singular", "sol": "Zero determinant means non-invertible (singular) matrix."},
            {"q": "de Broglie wavelength λ equals:", "options": ["h·p", "h/p", "p/h", "h/p²"], "ans": "h/p", "sol": "λ = h / p where h is Planck's constant."}
        ]
    }
}

# Full Branch -> Year -> Subject Hierarchy
BTECH_CURRICULUM = {
    "CSE & IT": {
        "1st Year (Foundation)": FIRST_YEAR_SUBJECTS,
        "2nd Year (Core)": {
            "Data Structures & Algorithms": {
                "concept": "Arrays, Linked Lists, Stacks, Queues, Binary Search Trees, Graph traversals (BFS/DFS), and sorting algorithms.",
                "exam_tips": "• Write step-by-step dry runs for Tree traversals and Dijkstra's shortest path.\n• Always include Best, Average, and Worst-case Big-O complexities.",
                "formulas": "Binary Search: O(log n) | Merge Sort: O(n log n) | Quick Sort Worst: O(n²)",
                "viva": [("LIFO vs FIFO?", "Stack uses LIFO; Queue uses FIFO."), ("Which traversal gives sorted BST?", "Inorder traversal (Left-Root-Right).")],
                "questions": [
                    {"q": "Which data structure follows LIFO?", "options": ["Queue", "Stack", "Graph", "Tree"], "ans": "Stack", "sol": "Stack pops the most recently pushed element first."},
                    {"q": "Worst-case time complexity of Quick Sort?", "options": ["O(n log n)", "O(n)", "O(n²)", "O(log n)"], "ans": "O(n²)", "sol": "Occurs when pivot is always smallest or largest element."},
                    {"q": "Which BST traversal yields sorted elements?", "options": ["Preorder", "Inorder", "Postorder", "Level-order"], "ans": "Inorder", "sol": "Inorder visits Left → Root → Right in ascending order."},
                    {"q": "BFS uses which data structure?", "options": ["Stack", "Queue", "Heap", "Set"], "ans": "Queue", "sol": "Queue processes nodes level by level in FIFO order."},
                    {"q": "Time complexity of Binary Search?", "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"], "ans": "O(log n)", "sol": "Search space halves at every step."}
                ]
            },
            "Operating Systems": {
                "concept": "Process lifecycle, CPU scheduling (FCFS, SJF, Round Robin), deadlocks, paging, and virtual memory.",
                "exam_tips": "• Practice Gantt charts for CPU scheduling numericals.\n• Memorize Coffman's 4 deadlock conditions and Banker's Algorithm.",
                "formulas": "TAT = Completion Time - Arrival Time | WT = TAT - Burst Time",
                "viva": [("What is Thrashing?", "Excessive paging where CPU spends more time swapping than executing."), ("What is a Semaphore?", "A synchronization variable used to prevent race conditions.")],
                "questions": [
                    {"q": "Which is NOT a deadlock condition?", "options": ["Mutual Exclusion", "Hold & Wait", "Preemption", "Circular Wait"], "ans": "Preemption", "sol": "Deadlock requires 'No Preemption'."},
                    {"q": "Convoy effect occurs in:", "options": ["Round Robin", "FCFS", "SJF", "Priority"], "ans": "FCFS", "sol": "Short processes wait behind one long process in FCFS."},
                    {"q": "Virtual memory is typically implemented using:", "options": ["Demand Paging", "Registers", "Cache", "ROM"], "ans": "Demand Paging", "sol": "Loads pages into RAM only when needed."},
                    {"q": "Turnaround Time equals:", "options": ["CT - AT", "CT + AT", "BT - AT", "WT - BT"], "ans": "CT - AT", "sol": "Completion Time minus Arrival Time."},
                    {"q": "Which scheduler selects processes from ready queue for CPU?", "options": ["Long-term", "Short-term", "Medium-term", "I/O"], "ans": "Short-term", "sol": "Short-term (CPU) scheduler dispatches ready processes."}
                ]
            }
        },
        "3rd Year (Advanced)": {
            "DBMS & Computer Networks": {
                "concept": "ER diagrams, SQL, Normalization (1NF–BCNF), ACID transactions, OSI/TCP-IP layers, IP routing, and TCP vs UDP.",
                "exam_tips": "• Practice finding candidate keys and decomposing tables into 3NF/BCNF.\n• Compare OSI 7 layers with TCP/IP 4 layers in tabular format.",
                "formulas": "IPv4: 32-bit | IPv6: 128-bit | ACID: Atomicity, Consistency, Isolation, Durability",
                "viva": [("TRUNCATE vs DELETE?", "TRUNCATE is DDL (faster, no rollback); DELETE is DML (row-by-row)."), ("Why is UDP faster than TCP?", "UDP is connectionless with no handshake or retransmission.")],
                "questions": [
                    {"q": "Which OSI layer handles IP routing?", "options": ["Data Link", "Network", "Transport", "Session"], "ans": "Network", "sol": "Layer 3 (Network) handles logical addressing and routing."},
                    {"q": "In ACID, 'I' stands for:", "options": ["Integrity", "Isolation", "Indexing", "Instance"], "ans": "Isolation", "sol": "Ensures concurrent transactions don't interfere."},
                    {"q": "Which normal form removes transitive dependency?", "options": ["1NF", "2NF", "3NF", "4NF"], "ans": "3NF", "sol": "3NF eliminates non-prime attributes depending on other non-prime attributes."},
                    {"q": "Which protocol resolves IP address to MAC address?", "options": ["DNS", "ARP", "DHCP", "ICMP"], "ans": "ARP", "sol": "Address Resolution Protocol maps IP to physical MAC."},
                    {"q": "Port number of HTTP is:", "options": ["21", "22", "80", "443"], "ans": "80", "sol": "HTTP uses port 80; HTTPS uses 443."}
                ]
            }
        },
        "4th Year (GATE & Placement)": {
            "Machine Learning & System Design": {
                "concept": "Supervised vs Unsupervised learning, regression, classification, overfitting, load balancers, caching, and microservices.",
                "exam_tips": "• Explain Bias-Variance tradeoff with clear diagrams.\n• For System Design, always discuss Horizontal Scaling, Caching (Redis), and Database Sharding.",
                "formulas": "Accuracy = (TP+TN)/Total | F1 = 2·(Precision·Recall)/(Precision+Recall)",
                "viva": [("Overfitting vs Underfitting?", "Overfitting memorizes training noise (high variance); underfitting fails to capture patterns (high bias)."), ("What is Horizontal Scaling?", "Adding more servers/machines rather than upgrading a single machine's CPU/RAM.")],
                "questions": [
                    {"q": "Predicting continuous house prices is:", "options": ["Classification", "Regression", "Clustering", "Dimensionality Reduction"], "ans": "Regression", "sol": "Continuous numeric output prediction is Regression."},
                    {"q": "K-Means is what type of algorithm?", "options": ["Supervised", "Unsupervised", "Reinforcement", "Semi-supervised"], "ans": "Unsupervised", "sol": "K-Means clusters unlabeled data."},
                    {"q": "Which technique prevents overfitting in neural networks?", "options": ["Dropout", "Increasing epochs", "Removing validation set", "Zero learning rate"], "ans": "Dropout", "sol": "Dropout randomly deactivates neurons during training."},
                    {"q": "Which component distributes incoming traffic across multiple servers?", "options": ["Compiler", "Load Balancer", "DNS Cache", "Firewall"], "ans": "Load Balancer", "sol": "Load balancers prevent single-server overload."},
                    {"q": "Metric best suited for imbalanced classification datasets:", "options": ["Raw Accuracy", "F1-Score", "Mean Squared Error", "R² Score"], "ans": "F1-Score", "sol": "F1 balances Precision and Recall on skewed classes."}
                ]
            }
        }
    },
    "ECE & EEE": {
        "1st Year (Foundation)": FIRST_YEAR_SUBJECTS,
        "2nd Year (Core)": {
            "Digital Electronics & Analog Circuits": {
                "concept": "Boolean algebra, K-Maps, combinational circuits (MUX, Adder), flip-flops, counters, diodes, and BJT/Op-Amp circuits.",
                "exam_tips": "• Check 'Don't Care' (X) terms while simplifying K-Maps.\n• Draw clean timing diagrams for sequential counters.",
                "formulas": "De Morgan: (A+B)' = A'B' | Mod-N Counter: 2ⁿ ≥ N | Inverting Op-Amp Gain: -Rf/Rin",
                "viva": [("Latch vs Flip-Flop?", "Latch is level-triggered; Flip-flop is edge-triggered."), ("Universal Gates?", "NAND and NOR gates.")],
                "questions": [
                    {"q": "Which gates are Universal Gates?", "options": ["AND & OR", "NAND & NOR", "XOR & XNOR", "NOT & OR"], "ans": "NAND & NOR", "sol": "Any Boolean circuit can be built using only NAND or only NOR."},
                    {"q": "Flip-flops needed for a Mod-16 counter:", "options": ["2", "3", "4", "8"], "ans": "4", "sol": "2⁴ = 16 states require 4 flip-flops."},
                    {"q": "In forward bias, PN junction depletion width:", "options": ["Increases", "Decreases", "Constant", "Infinite"], "ans": "Decreases", "sol": "Applied voltage reduces barrier potential."},
                    {"q": "Which flip-flop removes the invalid state of SR?", "options": ["D", "JK", "T", "Latch"], "ans": "JK", "sol": "JK toggles when J=1, K=1."},
                    {"q": "Binary of decimal 13 is:", "options": ["1011", "1101", "1110", "1001"], "ans": "1101", "sol": "8 + 4 + 0 + 1 = 1101."}
                ]
            }
        },
        "3rd Year (Advanced)": {
            "Signals, Systems & Microprocessors": {
                "concept": "Fourier & Laplace transforms, LTI systems, Nyquist sampling theorem, and 8085/8086 microprocessor architecture.",
                "exam_tips": "• Always state Region of Convergence (ROC) in Laplace & Z-transform problems.\n• Memorize 8085 flag register bits and addressing modes.",
                "formulas": "Nyquist Rate: fs ≥ 2·fm | 8085 Data Bus: 8-bit, Address Bus: 16-bit (64 KB memory)",
                "viva": [("What is Aliasing?", "Overlap of frequency spectra caused by sampling below Nyquist rate."), ("Role of Program Counter (PC)?", "Holds the memory address of the next instruction to be fetched.")],
                "questions": [
                    {"q": "Minimum sampling rate to avoid aliasing is:", "options": ["fm", "2·fm", "fm/2", "4·fm"], "ans": "2·fm", "sol": "Nyquist rate is twice the maximum signal frequency."},
                    {"q": "Width of 8085 microprocessor address bus:", "options": ["8-bit", "16-bit", "32-bit", "64-bit"], "ans": "16-bit", "sol": "16-bit address bus accesses 2¹⁶ = 64 KB memory."},
                    {"q": "An LTI system is stable if its impulse response is:", "options": ["Absolutely summable/integrable", "Unbounded", "Periodic", "Zero"], "ans": "Absolutely summable/integrable", "sol": "BIBO stability requires ∫|h(t)|dt < ∞."},
                    {"q": "Which transform converts differential equations into algebraic equations?", "options": ["Laplace Transform", "DFT", "Hilbert", "Wavelet"], "ans": "Laplace Transform", "sol": "Laplace transforms time-domain derivatives into s-domain multiplication."},
                    {"q": "8085 has how many hardware interrupts?", "options": ["2", "3", "5", "8"], "ans": "5", "sol": "TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR."}
                ]
            }
        },
        "4th Year (GATE & Placement)": {
            "VLSI Design & Embedded Systems": {
                "concept": "CMOS logic design, stick diagrams, fabrication steps, RTOS scheduling, and communication protocols (UART, SPI, I2C).",
                "exam_tips": "• Draw pull-up (PMOS) and pull-down (NMOS) networks clearly for CMOS gate questions.\n• Compare SPI, I2C, and UART by wire count and speed.",
                "formulas": "CMOS Static Power ≈ 0 | Dynamic Power: P = α · C · Vdd² · f",
                "viva": [("Why is CMOS preferred over NMOS?", "CMOS consumes near-zero static power because pull-up and pull-down paths are never ON simultaneously."), ("I2C vs SPI?", "I2C uses 2 wires (SDA, SCL); SPI uses 4 wires and is faster.")],
                "questions": [
                    {"q": "In CMOS inverter, which transistor is at the top (connected to Vdd)?", "options": ["NMOS", "PMOS", "BJT", "JFET"], "ans": "PMOS", "sol": "PMOS pulls output high to Vdd; NMOS pulls low to GND."},
                    {"q": "How many wires does I2C protocol use?", "options": ["1", "2", "3", "4"], "ans": "2", "sol": "SDA (Serial Data) and SCL (Serial Clock)."},
                    {"q": "Dynamic power in CMOS is proportional to:", "options": ["Vdd", "Vdd²", "1/Vdd", "√Vdd"], "ans": "Vdd²", "sol": "P_dyn = α · C · Vdd² · f."},
                    {"q": "Which protocol is full-duplex with 4 wires (MOSI, MISO, SCLK, SS)?", "options": ["UART", "I2C", "SPI", "CAN"], "ans": "SPI", "sol": "Serial Peripheral Interface uses 4 lines."},
                    {"q": "Moore's Law states transistor count doubles roughly every:", "options": ["6 months", "18–24 months", "5 years", "10 years"], "ans": "18–24 months", "sol": "Gordon Moore observed doubling every ~2 years."}
                ]
            }
        }
    },
    "Mechanical Engineering": {
        "1st Year (Foundation)": FIRST_YEAR_SUBJECTS,
        "2nd Year (Core)": {
            "Thermodynamics & Strength of Materials": {
                "concept": "Laws of thermodynamics, Carnot/Otto/Diesel cycles, entropy, stress-strain curves, SFD & BMD for beams.",
                "exam_tips": "• Draw Free Body Diagrams (FBD) before plotting SFD & BMD.\n• Always write SI units (kPa, kJ/kg, MPa) in numericals.",
                "formulas": "1st Law: δQ = dU + δW | Carnot η = 1 - T₂/T₁ | Hooke's Law: σ = E·ε",
                "viva": [("Zeroth Law defines?", "Temperature and thermal equilibrium."), ("Point of contraflexure?", "Where Bending Moment is zero and changes sign.")],
                "questions": [
                    {"q": "Which law defines Temperature?", "options": ["Zeroth Law", "First Law", "Second Law", "Third Law"], "ans": "Zeroth Law", "sol": "Forms the basis of thermometry."},
                    {"q": "Entropy remains constant in which process?", "options": ["Isobaric", "Isochoric", "Isentropic", "Isothermal"], "ans": "Isentropic", "sol": "Reversible adiabatic process has ΔS = 0."},
                    {"q": "Ratio of lateral strain to linear strain is:", "options": ["Young's Modulus", "Poisson's Ratio", "Bulk Modulus", "Rigidity Modulus"], "ans": "Poisson's Ratio", "sol": "ν = - (Lateral strain / Axial strain)."},
                    {"q": "At point of contraflexure, which is zero?", "options": ["Shear Force", "Bending Moment", "Load", "Slope"], "ans": "Bending Moment", "sol": "BM changes from sagging to hogging."},
                    {"q": "Maximum theoretical efficiency cycle:", "options": ["Otto", "Diesel", "Carnot", "Rankine"], "ans": "Carnot", "sol": "Carnot cycle is completely reversible."}
                ]
            }
        },
        "3rd Year (Advanced)": {
            "Fluid Mechanics & Heat Transfer": {
                "concept": "Bernoulli's equation, Reynolds number, boundary layer, conduction (Fourier's law), convection, and radiation.",
                "exam_tips": "• Memorize dimensionless numbers (Reynolds, Nusselt, Prandtl) and their physical meanings.\n• State assumptions before deriving Bernoulli's equation.",
                "formulas": "Re = ρVD/μ | Fourier's Law: Q = -kA(dT/dx) | Stefan-Boltzmann: E = σT⁴",
                "viva": [("Laminar vs Turbulent flow in pipe?", "Re < 2000 is laminar; Re > 4000 is turbulent."), ("What is a Blackbody?", "An ideal body that absorbs 100% of incident thermal radiation.")],
                "questions": [
                    {"q": "Pipe flow is laminar when Reynolds number (Re) is:", "options": ["< 2000", "> 4000", "> 10000", "= 5000"], "ans": "< 2000", "sol": "Viscous forces dominate below Re = 2000."},
                    {"q": "Conduction heat transfer is governed by:", "options": ["Newton's Law", "Fourier's Law", "Stefan-Boltzmann Law", "Pascal's Law"], "ans": "Fourier's Law", "sol": "Q = -kA(dT/dx)."},
                    {"q": "Bernoulli's equation is based on conservation of:", "options": ["Mass", "Momentum", "Energy", "Angular Momentum"], "ans": "Energy", "sol": "Sum of pressure, kinetic, and potential heads is constant."},
                    {"q": "Unit of dynamic viscosity is:", "options": ["Pa·s (or Poise)", "m²/s", "N/m", "W/m·K"], "ans": "Pa·s (or Poise)", "sol": "1 Pa·s = 10 Poise."},
                    {"q": "Radiation heat transfer is proportional to:", "options": ["T", "T²", "T³", "T⁴"], "ans": "T⁴", "sol": "Stefan-Boltzmann law: E = σT⁴."}
                ]
            }
        },
        "4th Year (GATE & Placement)": {
            "CAD/CAM, Robotics & Industrial Engg": {
                "concept": "CNC programming (G & M codes), robot kinematics (DOF), PERT/CPM project management, and Lean/Six Sigma.",
                "exam_tips": "• Practice critical path and float calculations in PERT/CPM.\n• Memorize common G-codes (G00, G01, G02, G03) and M-codes (M03, M05, M30).",
                "formulas": "PERT Expected Time: te = (to + 4tm + tp)/6 | EOQ = √(2DS/H)",
                "viva": [("Difference between PERT and CPM?", "PERT is probabilistic (R&D projects); CPM is deterministic (construction/routine)."), ("What is DOF in Robotics?", "Number of independent motions/axes a robot manipulator can perform.")],
                "questions": [
                    {"q": "Which G-code stands for linear interpolation in CNC?", "options": ["G00", "G01", "G02", "G04"], "ans": "G01", "sol": "G00 is rapid positioning; G01 is linear feed interpolation."},
                    {"q": "Critical Path in CPM has total float equal to:", "options": ["Zero", "Maximum", "Negative", "Infinity"], "ans": "Zero", "sol": "Critical activities cannot be delayed without delaying the project."},
                    {"q": "PERT time distribution follows:", "options": ["Normal", "Beta", "Poisson", "Binomial"], "ans": "Beta", "sol": "PERT uses Beta distribution with 3 time estimates."},
                    {"q": "Six Sigma aims for defects per million opportunities (DPMO) below:", "options": ["3.4", "34", "340", "3400"], "ans": "3.4", "sol": "Six Sigma corresponds to 99.99966% defect-free output."},
                    {"q": "Which CNC code ends the program and resets?", "options": ["M00", "M03", "M06", "M30"], "ans": "M30", "sol": "M30 indicates end of tape/program and rewind."}
                ]
            }
        }
    },
    "Civil Engineering": {
        "1st Year (Foundation)": FIRST_YEAR_SUBJECTS,
        "2nd Year (Core)": {
            "Surveying & Building Materials": {
                "concept": "Chain & compass surveying, leveling, theodolite, cement properties, concrete mix design, and brick masonry.",
                "exam_tips": "• Practice Rise & Fall vs Height of Instrument (HI) leveling table checks.\n• Memorize initial & final setting times of Ordinary Portland Cement (OPC).",
                "formulas": "HI = RL + BS | Check: ΣBS - ΣFS = Last RL - First RL | OPC Initial Setting: ≥ 30 mins",
                "viva": [("Benchmark (BM) in surveying?", "A fixed reference point of known elevation (Reduced Level)."), ("Why is gypsum added to cement?", "To retard flash setting and control initial setting time.")],
                "questions": [
                    {"q": "Initial setting time of Ordinary Portland Cement (OPC) is:", "options": ["10 mins", "30 mins", "2 hours", "10 hours"], "ans": "30 mins", "sol": "Minimum initial setting time is 30 minutes; final is 10 hours."},
                    {"q": "First staff reading taken after setting up a level is:", "options": ["Foresight (FS)", "Backsight (BS)", "Intermediate Sight", "Datum"], "ans": "Backsight (BS)", "sol": "BS is taken on a point of known RL."},
                    {"q": "Workability of concrete is commonly measured by:", "options": ["Slump Test", "Vicat Apparatus", "Le Chatelier", "Los Angeles Test"], "ans": "Slump Test", "sol": "Slump cone measures fresh concrete consistency/workability."},
                    {"q": "Whole Circle Bearing (WCB) varies from:", "options": ["0° to 90°", "0° to 180°", "0° to 360°", "-90° to +90°"], "ans": "0° to 360°", "sol": "Measured clockwise from North."},
                    {"q": "Constituent providing maximum strength to cement:", "options": ["C3S (Alite)", "C2S", "C3A", "C4AF"], "ans": "C3S (Alite)", "sol": "Tricalcium silicate (C3S) gives early and high strength."}
                ]
            }
        },
        "3rd Year (Advanced)": {
            "Structural Analysis & Geotechnical Engg": {
                "concept": "Indeterminate beams, slope-deflection, soil classification, permeability (Darcy's law), consolidation, and shear strength.",
                "exam_tips": "• Draw Mohr's circle clearly for soil shear strength problems.\n• Check static & kinematic indeterminacy formulas.",
                "formulas": "Darcy's Law: q = k·i·A | Terzaghi Effective Stress: σ' = σ - u | Void Ratio: e = Vv/Vs",
                "viva": [("What is Quick Sand condition?", "When upward seepage pressure equals submerged unit weight of soil, making effective stress zero."), ("Porosity vs Void Ratio?", "Porosity n = Vv/V; Void ratio e = Vv/Vs.")],
                "questions": [
                    {"q": "Darcy's Law is valid for which type of flow in soils?", "options": ["Laminar", "Turbulent", "Transitional", "Supersonic"], "ans": "Laminar", "sol": "Valid for low-velocity laminar seepage."},
                    {"q": "Effective stress in saturated soil equals:", "options": ["σ + u", "σ - u", "u - σ", "σ · u"], "ans": "σ - u", "sol": "Total stress minus pore water pressure (Terzaghi's principle)."},
                    {"q": "Relation between void ratio (e) and porosity (n):", "options": ["n = e/(1+e)", "n = e/(1-e)", "e = n/(1+n)", "n = 1+e"], "ans": "n = e/(1+e)", "sol": "Standard phase relationship in soil mechanics."},
                    {"q": "Degree of static indeterminacy of a fixed beam is:", "options": ["0", "1", "2", "3"], "ans": "3", "sol": "6 reactions minus 3 equilibrium equations = 3."},
                    {"q": "Liquid Limit of soil is determined using:", "options": ["Casagrande Apparatus", "Pycnometer", "Oedometer", "Hydrometer"], "ans": "Casagrande Apparatus", "sol": "Measures water content at 25 blows."}
                ]
            }
        },
        "4th Year (GATE & Placement)": {
            "Transportation & Environmental Engg": {
                "concept": "Highway geometric design (superelevation, sight distance), water treatment, BOD/COD, and air pollution control.",
                "exam_tips": "• Memorize IRC recommended values for camber, ruling gradient, and superelevation.\n• Practice 5-day BOD numericals.",
                "formulas": "Superelevation: e + f = V²/(127R) | BOD₅ = (DO_initial - DO_final) × Dilution Factor",
                "viva": [("BOD vs COD?", "BOD is biodegradable organic matter decomposed by bacteria; COD measures both biodegradable and non-biodegradable organics."), ("Why is superelevation provided?", "To counteract centrifugal force on horizontal road curves.")],
                "questions": [
                    {"q": "Maximum superelevation in plain & rolling terrain (IRC):", "options": ["4%", "7%", "10%", "15%"], "ans": "7%", "sol": "IRC specifies 7% (0.07) for plain terrain and 10% for hills."},
                    {"q": "Standard BOD test is conducted at 20°C for:", "options": ["1 day", "3 days", "5 days", "10 days"], "ans": "5 days", "sol": "5-day BOD (BOD₅) is the global standard."},
                    {"q": "Disinfection of drinking water commonly uses:", "options": ["Alum", "Chlorine", "Activated Carbon", "Lime"], "ans": "Chlorine", "sol": "Chlorination kills pathogenic bacteria."},
                    {"q": "Stopping Sight Distance (SSD) equals:", "options": ["Lag distance + Braking distance", "Lag - Braking", "2 × Braking distance", "Only Lag distance"], "ans": "Lag distance + Braking distance", "sol": "Distance traveled during reaction time plus braking."},
                    {"q": "pH of neutral drinking water is:", "options": ["4.5", "7.0", "9.5", "11.0"], "ans": "7.0", "sol": "Acceptable drinking water pH range is 6.5 to 8.5."}
                ]
            }
        }
    }
}

# 5 Cross-Branch Aptitude Questions to complete 10-Question Mock Test
EXTRA_APTITUDE_BANK = [
    {"q": "What is the SI unit of electrical conductance?", "options": ["Ohm", "Siemens (Mho)", "Henry", "Farad"], "ans": "Siemens (Mho)", "sol": "Conductance is reciprocal of resistance (1/Ω)."},
    {"q": "Which sorting algorithm guarantees O(n log n) in worst case?", "options": ["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"], "ans": "Merge Sort", "sol": "Merge Sort always divides array in half with O(n log n) complexity."},
    {"q": "Derivative of ln(x) with respect to x is:", "options": ["x", "1/x", "e^x", "1/x²"], "ans": "1/x", "sol": "d/dx [ln(x)] = 1/x."},
    {"q": "Which protocol dynamically assigns IP addresses?", "options": ["DNS", "DHCP", "HTTP", "ARP"], "ans": "DHCP", "sol": "Dynamic Host Configuration Protocol assigns IPs automatically."},
    {"q": "In mechanics, a couple produces:", "options": ["Pure translation", "Pure rotation", "Both", "Zero motion"], "ans": "Pure rotation", "sol": "Equal and opposite parallel forces create pure rotational moment."}
]

# Sidebar Navigation: Branch -> Year -> Subject
with st.sidebar:
    st.header("🎯 Select Branch & Year")
    selected_branch = st.selectbox("1. B.Tech Branch", list(BTECH_CURRICULUM.keys()))
    selected_year = st.selectbox("2. Academic Year", list(BTECH_CURRICULUM[selected_branch].keys()))
    selected_subject = st.selectbox("3. Subject", list(BTECH_CURRICULUM[selected_branch][selected_year].keys()))

    st.divider()
    st.subheader("🏆 Study XP & Rank")
    xp_box = st.empty()
    rank_box = st.empty()

    st.divider()
    st.subheader("⏱️ Deep Focus Timer")
    if st.button("▶️ Start 25-Min Focus Sprint", use_container_width=True):
        bar = st.progress(0)
        for p in range(1, 101):
            time.sleep(0.01)
            bar.progress(p)
        st.success("🎉 Focus Sprint Complete! +15 XP!")

sub_data = BTECH_CURRICULUM[selected_branch][selected_year][selected_subject]

# Hero Banner
st.markdown(f"""
<div class="hero-banner">
    <h1 style="margin:0;">🎓 B.Tech All-Branch & Year-Wise AI Study Hub</h1>
    <p style="margin:6px 0 0 0; opacity:0.95;">Built by <b>Vivekanand Pandey</b> • Global AI Hackathon</p>
    <div class="badge-pill">🏫 {selected_branch} &nbsp;|&nbsp; 📅 {selected_year} &nbsp;|&nbsp; 📘 {selected_subject}</div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Concepts, Formulas & Exam Tips",
    "🧠 10-Question Exam Quiz",
    "📅 Smart Study Planner",
    "⚡ Viva Wheel & Grade Calc"
])

# TAB 1: CONCEPTS + EXAM TIPS + FORMULAS
with tab1:
    st.subheader(f"📖 {selected_subject} ({selected_branch} — {selected_year})")
    
    st.markdown("### 1. Core Concept Summary")
    st.markdown(f'<div class="concept-card">{sub_data["concept"]}</div>', unsafe_allow_html=True)

    st.markdown("### 2. University Exam-Oriented Scoring Tips")
    tips_html = sub_data["exam_tips"].replace("\n", "<br>")
    st.markdown(f'<div class="tip-card">{tips_html}</div>', unsafe_allow_html=True)

    st.markdown("### 3. Must-Know Formulas & Quick Syntax")
    st.code(sub_data["formulas"], language="text")

    st.markdown("### 4. Rapid-Fire Viva Flashcards")
    for idx, (vq, va) in enumerate(sub_data["viva"], start=1):
        st.markdown(f'<div class="viva-card"><b>🎤 Viva Q{idx}:</b> {vq}</div>', unsafe_allow_html=True)
        with st.expander(f"👀 Reveal Answer for Viva Q{idx}"):
            st.write(f"**Answer:** {va}")

# TAB 2: 10-QUESTION EXAM QUIZ
with tab2:
    st.subheader(f"🧠 10-Question Exam Mock Test: {selected_subject}")
    st.caption("5 Core Subject Questions + 5 Engineering Aptitude Questions • Instant Solutions Included!")

    quiz_list = sub_data["questions"] + EXTRA_APTITUDE_BANK
    score = 0
    attempted = 0

    for i, item in enumerate(quiz_list, start=1):
        tag = "📘 Core Subject" if i <= 5 else "⚙️ Engineering Aptitude"
        st.markdown(f"**Q{i} [{tag}]. {item['q']}**")
        ans = st.radio(
            f"Q{i}",
            item["options"],
            index=None,
            key=f"{selected_branch}_{selected_year}_{selected_subject}_{i}",
            label_visibility="collapsed"
        )
        if ans is not None:
            attempted += 1
            if ans == item["ans"]:
                score += 1
                st.success(f"✅ **Right Answer! (+20 XP)** {item['sol']}")
            else:
                st.error(f"❌ **Wrong Answer!** Correct Option: **{item['ans']}**\n\n💡 **Solution:** {item['sol']}")
        st.write("")

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Attempted", f"{attempted} / 10")
    c2.metric("Score", f"{score} / 10")
    c3.metric("Accuracy", f"{int((score/attempted)*100) if attempted > 0 else 0}%")

    if score == 10:
        st.balloons()
        st.success("🏆 10/10 PERFECT SCORE! Gold Medalist Level Unlocked!")

# TAB 3: STUDY PLANNER & DOWNLOAD
with tab3:
    st.subheader(f"📅 Exam Preparation Planner: {selected_subject}")
    col1, col2 = st.columns(2)
    with col1:
        days = st.number_input("Days Left for Exam", 1, 120, 14)
    with col2:
        hours = st.number_input("Daily Study Hours", 1, 16, 3)

    if st.button("🚀 Generate Study Plan", use_container_width=True):
        s_days = max(1, int(days * 0.65))
        p_days = max(1, int(days * 0.25))
        r_days = max(0, days - s_days - p_days)
        st.success(f"**{days}-Day Roadmap ({days*hours} Total Hours):**")
        st.write(f"• **Days 1–{s_days}:** Core Concepts & Derivations ({s_days*hours} hrs)")
        st.write(f"• **Days {s_days+1}–{s_days+p_days}:** Last 5-Year University PYQs ({p_days*hours} hrs)")
        st.write(f"• **Final {r_days} Days:** Formula Sheet & 10-Q Mock Quiz")

        plan_txt = f"STUDY PLAN: {selected_subject} ({selected_branch} - {selected_year})\nDays: {days} | Daily Hours: {hours}\n\nTips:\n{sub_data['exam_tips']}"
        st.download_button("📥 Download Plan (.txt)", data=plan_txt, file_name=f"{selected_subject}_Plan.txt")

    st.divider()
    st.subheader("✅ Readiness Checklist (+25 XP each)")
    chk1 = st.checkbox("Completed Module Notes")
    chk2 = st.checkbox("Practiced Numericals / Programs")
    chk3 = st.checkbox("Solved PYQs")
    chk4 = st.checkbox("Completed 10-Q Mock Test")
    chk_xp = sum([chk1, chk2, chk3, chk4]) * 25
    st.progress(chk_xp / 100, text=f"Readiness: {chk_xp}%")

# TAB 4: SPIN THE VIVA WHEEL & GRADE CALCULATOR
with tab4:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("🎲 Spin the Viva Challenge Wheel")
        if st.button("🎰 Spin Random Question!", use_container_width=True):
            all_v = [v for b in BTECH_CURRICULUM.values() for y in b.values() for s in y.values() for v in s["viva"]]
            rq, ra = random.choice(all_v)
            st.warning(f"**Challenge:** {rq}")
            st.info(f"**Answer:** {ra}")

    with col_b:
        st.subheader("📊 Semester Grade Target Calculator")
        mid_marks = st.slider("Internal / Mid-Sem Marks (out of 30)", 0, 30, 22)
        target = st.selectbox("Target Total (out of 100)", [90, 80, 70, 60, 40])
        req = target - mid_marks
        if req <= 70:
            st.success(f"🎯 You need **{req} / 70** in End-Sem to score {target}+!")
        else:
            st.warning(f"⚠️ Max possible total is {mid_marks + 70}.")

# Update Live XP in Sidebar
total_xp = chk_xp + (score * 20)
rank = "🏆 Exam Topper" if total_xp >= 200 else "🔥 Semester Pro" if total_xp >= 120 else "⚡ Lab Warrior" if total_xp >= 50 else "🌱 Fresher"
xp_box.metric("Total XP", f"{total_xp} XP")
rank_box.info(f"**Rank:** {rank}")
