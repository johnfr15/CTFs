import os
import subprocess

# Define the base flag and expected output
prefix = '    parameter FLAG_TO_TEST = "0ops{aadc337c'
index = 13
suffix = '",\n'
expected_output = "30789d5692f2fe23bb2c5d9e16406653b6cb217c952998ce17b7143788d949952680b4bce4c30a96c753"
allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-|?!$^*/{}"
vf_path = "./EzLogic/problem/EzLogic_tb.v"

verilog_files = [
    "./EzLogic/models/BUFG.v",
    "./EzLogic/models/CARRY4.v",
    "./EzLogic/models/FDCE.v",
    "./EzLogic/models/GND.v",
    "./EzLogic/models/IBUF.v",
    "./EzLogic/models/LUT1.v",
    "./EzLogic/models/LUT2.v",
    "./EzLogic/models/LUT3.v",
    "./EzLogic/models/LUT4.v",
    "./EzLogic/models/LUT5.v",
    "./EzLogic/models/LUT6.v",
    "./EzLogic/models/MUXF7.v",
    "./EzLogic/models/MUXF8.v",
    "./EzLogic/models/OBUF.v",
    "./EzLogic/models/VCC.v",
    "./EzLogic/problem/EzLogic_tb.v",  # Testbench file
    "./EzLogic/problem/EzLogic_top_synth.v"  # Top module file
]

def test(prefix: str, char: str, suffix: str):
    """
    Modifies the FLAG_TO_TEST parameter in the testbench Verilog file.
    """
    with open(vf_path, "r") as file:
        lines = file.readlines()
    lines[3] = f'{prefix}{char}{suffix}'
    with open(vf_path, "w") as file:
        file.write("".join(lines))

def compile_and_run(index: int):
    """
    Compiles and runs the Verilog testbench using iverilog and vvp.
    Returns the simulation output.
    """
    try:
        # Compile the Verilog files
        subprocess.run(["iverilog", "-o", "solve"] + verilog_files, check=True)
        # Run the simulation
        result = subprocess.run(["vvp", "./solve"], stdout=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split("\n")[2][-((index+1)*2):]
        return output
    except subprocess.CalledProcessError as e:
        print("Error during compilation or simulation:", e)
        return ""

if __name__ == "__main__":

    i = 0
    while allowed_characters[i] != "}":
        char = allowed_characters[i]

        test(prefix, char, suffix)
        output = compile_and_run(index)

        if output in expected_output:
            i = -1
            index += 1
            prefix += char
            print(f"{expected_output}\n{output}\n{prefix}")
        i+=1