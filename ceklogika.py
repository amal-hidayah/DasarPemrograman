input1 = "Hello"
input2 = 10
input3 = 3.14

if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
    print("Tipe input valid")
else:
    print("Tipe input tidak valid")

test_cases = [
    (192, 16, 8.12),       
    ("Amal", "12", 1.91), 
    ("Ganteng", 12, "1.90"), 
    ("Amalganteng", 19, 1.2) 
]

for i, case in enumerate(test_cases, 1):
    input1, input2, input3 = case
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        print(f"Kasus uji {i}: {case} -> Tipe input valid")
    else:
        print(f"Kasus uji {i}: {case} -> Tipe input tidak valid")
