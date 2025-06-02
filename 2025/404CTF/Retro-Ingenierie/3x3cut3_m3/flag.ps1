$keyArray = @(42, 17, 99, 84, 63, 19, 88, 7, 31, 55, 91, 12, 33, 20, 75, 11)
$targetArray = @(93, 72, 28, 24, 67, 23, 98, 58, 35, 75, 98, 87, 68, 30, 97, 33)
$usernameLength = ("ElPouleto").Length

# Will store all matching characters for each position
$foundPassword = ""

# Loop over each index of the target array
for ($i = 0; $i -lt $targetArray.Length; $i++) {
    $foundChar = $null

    # Try every printable ASCII character (space to ~)
    for ($ascii = 32; $ascii -le 126; $ascii++) {
        $charCode = $ascii
        $encodedVal = (($charCode -bxor $keyArray[$i]) - $usernameLength) % 169
        if ($encodedVal -lt 0) { $encodedVal += 169 }

        if ($encodedVal -eq $targetArray[$i]) {
            $foundChar = [char]$charCode
            break
        }
    }

    if ($foundChar) {
        Write-Host "Position ${i}: Found '${foundChar}'"
        $foundPassword += $foundChar
    } else {
        Write-Host "Position ${i}: No match found!" -ForegroundColor Red
        $foundPassword += '?'
    }
}

Write-Host "`nRecovered Password: ${foundPassword}" -ForegroundColor Green
