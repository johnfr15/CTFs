# Key array used for XOR operations
$keyArray = @(42, 17, 99, 84, 63, 19, 88, 7, 31, 55, 91, 12, 33, 20, 75, 11)

# Length of the current username
$usernameLength = ($env:USERNAME).Length

# Prompt user to enter the password
$passwordInput = Read-Host -Prompt ([System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String("VmV1aWxsZXogZW50cmVyIGxlIG1vdCBkZSBwYXNzZSBwb3VyIGZhaXJlIGTpY29sbGVyIGxhIGZ1c+ll")))

# Prepare an array to hold the decoded integer values
$decodedInput = @()

for ($i = 0; $i -lt $passwordInput.Length; $i++) {
    # Convert character to integer ASCII code
    $charCode = [int][char]$passwordInput[$i]

    # XOR with keyArray element, then subtract username length, modulo 169 (13^2)
    $val = (($charCode -bxor $keyArray[$i]) - $usernameLength) % [math]::Pow(13, 2)
    if ($val -lt 0) { $val += [math]::Pow(13, 2) } 

    $decodedInput += $val
}

# Predefined target array for validation
$targetArray = @(93, 72, 28, 24, 67, 23, 98, 58, 35, 75, 98, 87, 68, 30, 97, 33)

# Flag for whether the input matches the target
$isPasswordCorrect = $true

for ($i = 0; $i -lt $targetArray.Length; $i++) {
    if ($targetArray[$i] -ne $decodedInput[$i]) {
        $isPasswordCorrect = $false
        break
    }
}

if ($isPasswordCorrect) {
    # Password correct: play success beeps and show success message
    $successTune = @(
        (130, 100), (262, 100), (330, 100), (392, 100), (523, 100), (660, 100), (784, 300), (660, 300),
        (146, 100), (262, 100), (311, 100), (415, 100), (523, 100), (622, 100), (831, 300), (622, 300),
        (155, 100), (294, 100), (349, 100), (466, 100), (588, 100), (699, 100), (933, 300), (933, 100),
        (933, 100), (933, 100), (1047, 400)
    )
    foreach ($note in $successTune) { [Console]::Beep($note[0], $note[1]) }
    Write-Host ([System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String("TW90IGRlIHBhc3NlIGNvcnJlY3QgISBMYSBmdXPpZSBzJ2Vudm9sZWVlZSAh"))) -ForegroundColor Green
} else {
    # Password incorrect: send some keys, play failure beeps, and text-to-speech "Boom" + error message
    $shell = New-Object -ComObject wscript.shell
    1..50 | ForEach-Object { $shell.SendKeys([char]175) }

    $failureTune = @(
        @{ Pitch = 1059.274; Length = 300 },
        @{ Pitch = 1059.274; Length = 200 },
        @{ Pitch = 1188.995; Length = 500 },
        @{ Pitch = 1059.274; Length = 500 },
        @{ Pitch = 1413.961; Length = 500 },
        @{ Pitch = 1334.601; Length = 950 },
        @{ Pitch = 1059.274; Length = 300 },
        @{ Pitch = 1059.274; Length = 200 },
        @{ Pitch = 1188.995; Length = 500 },
        @{ Pitch = 1059.274; Length = 500 },
        @{ Pitch = 1587.117; Length = 500 },
        @{ Pitch = 1413.961; Length = 950 },
        @{ Pitch = 1059.274; Length = 300 },
        @{ Pitch = 1059.274; Length = 200 },
        @{ Pitch = 2118.547; Length = 500 },
        @{ Pitch = 1781.479; Length = 500 },
        @{ Pitch = 1413.961; Length = 500 },
        @{ Pitch = 1334.601; Length = 500 },
        @{ Pitch = 1188.995; Length = 500 },
        @{ Pitch = 1887.411; Length = 300 },
        @{ Pitch = 1887.411; Length = 200 },
        @{ Pitch = 1781.479; Length = 500 },
        @{ Pitch = 1413.961; Length = 500 },
        @{ Pitch = 1587.117; Length = 500 },
        @{ Pitch = 1413.961; Length = 900 }
    )

    foreach ($note in $failureTune) {
        [System.Console]::Beep($note['Pitch'], $note['Length'])
    }

    function Invoke-TextToSpeech($text) {
        Add-Type -AssemblyName System.speech
        $synthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
        $synthesizer.Speak($text)
    }
    Invoke-TextToSpeech "Boom"

    Write-Host ([System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String("TW90IGRlIHBhc3NlIGluY29ycmVjdC4gTGEgZnVz6WUgdmllbnQgZCdleHBsb3NlciA="))) -ForegroundColor Red

    # Minimize user32 window by sending message
    Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    public class User32 {
        [DllImport("user32.dll")]
        public static extern int SendMessage(int hWnd, int Msg, int wParam, int lParam);
    }
"@

    [User32]::SendMessage(-1, 0x0112, 0xF170, 2)
}
