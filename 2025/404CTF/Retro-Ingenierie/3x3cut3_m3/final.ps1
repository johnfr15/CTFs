$064534fb2d3645b296259adeb6f2f359 = @(42, 17, 99, 84, 63, 19, 88, 7, 31, 55, 91, 12, 33, 20, 75, 11)
$e9a52fde54d64826ac376a409f67e592 = ($env:USERNAME).Length

$271add1f5e06432994b33cbf742d6682 = Read-Host -Prompt  ([System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String("VmV1aWxsZXogZW50cmVyIGxlIG1vdCBkZSBwYXNzZSBwb3VyIGZhaXJlIGTpY29sbGVyIGxhIGZ1c+ll")))

$3ca127ca6cdf4d429c2373d9535141ff = @()
    for ($284aa2e829f946bdb78f32c695237d98 = 0; $284aa2e829f946bdb78f32c695237d98 -lt $271add1f5e06432994b33cbf742d6682.Length; $284aa2e829f946bdb78f32c695237d98++) {
        $0cae3e36a0c44306b62f72deb9a5e5e2 = [int][char]$271add1f5e06432994b33cbf742d6682[$284aa2e829f946bdb78f32c695237d98]
        $2242a5c393534797baffd2a854831810 = (($0cae3e36a0c44306b62f72deb9a5e5e2 -bxor $064534fb2d3645b296259adeb6f2f359[$284aa2e829f946bdb78f32c695237d98]) - $e9a52fde54d64826ac376a409f67e592) % [math]::Pow(13,2)
        if ($2242a5c393534797baffd2a854831810 -lt 0) { $2242a5c393534797baffd2a854831810 += [math]::Pow(13,2) } 
        $3ca127ca6cdf4d429c2373d9535141ff += $2242a5c393534797baffd2a854831810
    }

    $9514367d5ca84f4da65a355dd524ceee = @(93, 72, 28, 24, 67, 23, 98, 58, 35, 75, 98, 87, 68, 30, 97, 33)
$2a9b1948d9fd492c83b8d011a8bdcda7 = $true
for ($284aa2e829f946bdb78f32c695237d98 = 0; $284aa2e829f946bdb78f32c695237d98 -lt $9514367d5ca84f4da65a355dd524ceee.Length; $284aa2e829f946bdb78f32c695237d98++) {
    if ($9514367d5ca84f4da65a355dd524ceee[$284aa2e829f946bdb78f32c695237d98] -ne $3ca127ca6cdf4d429c2373d9535141ff[$284aa2e829f946bdb78f32c695237d98]) {
        $2a9b1948d9fd492c83b8d011a8bdcda7 = $false
        break
    }
}

if ($2a9b1948d9fd492c83b8d011a8bdcda7) {
    $b818610f1a504572b6af74f268620cc2 = @((130,100),(262,100),(330,100),(392,100),(523,100),(660,100),(784,300),(660,300),(146,100),(262,100),(311,100),(415,100),(523,100),(622,100),(831,300),(622,300),(155,100),(294,100),(349,100),(466,100),(588,100),(699,100),(933,300),(933,100),(933,100),(933,100),(1047,400))
    foreach ($N in $b818610f1a504572b6af74f268620cc2) { [Console]::Beep($N[0],$N[1]) }
    Write-Host ([System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String("TW90IGRlIHBhc3NlIGNvcnJlY3QgISBMYSBmdXPpZSBzJ2Vudm9sZWVlZSAh"))) -ForegroundColor Green
} else {
    $7d2001d954134742914aa6731ec558e2 = New-Object -com wscript.shell; 1..50 | % { $7d2001d954134742914aa6731ec558e2.SendKeys([char]175) }; 
    $09fefe8428234a6da050e9c186a8132c = @(
    @{ Pitch = 1059.274; Length = 300; };
    @{ Pitch = 1059.274; Length = 200; };
    @{ Pitch = 1188.995; Length = 500; };
    @{ Pitch = 1059.274; Length = 500; };
    @{ Pitch = 1413.961; Length = 500; };
    @{ Pitch = 1334.601; Length = 950; };

    @{ Pitch = 1059.274; Length = 300; };
    @{ Pitch = 1059.274; Length = 200; };
    @{ Pitch = 1188.995; Length = 500; };
    @{ Pitch = 1059.274; Length = 500; };
    @{ Pitch = 1587.117; Length = 500; };
    @{ Pitch = 1413.961; Length = 950; };

    @{ Pitch = 1059.274; Length = 300; };
    @{ Pitch = 1059.274; Length = 200; };
    @{ Pitch = 2118.547; Length = 500; };
    @{ Pitch = 1781.479; Length = 500; };
    @{ Pitch = 1413.961; Length = 500; };
    @{ Pitch = 1334.601; Length = 500; };
    @{ Pitch = 1188.995; Length = 500; };
    @{ Pitch = 1887.411; Length = 300; };
    @{ Pitch = 1887.411; Length = 200; };
    @{ Pitch = 1781.479; Length = 500; };
    @{ Pitch = 1413.961; Length = 500; };
    @{ Pitch = 1587.117; Length = 500; };
    @{ Pitch = 1413.961; Length = 900; };
    );

    foreach ($Beep in $09fefe8428234a6da050e9c186a8132c) {
        [System.Console]::Beep($Beep['Pitch'], $Beep['Length']);
    }
    Function Invoke-TextToSpeech($Text) { Add-Type -AssemblyName System.speech; $0b208177d5aa47c79e1f785faa9ae70b = New-Object System.Speech.Synthesis.SpeechSynthesizer; $0b208177d5aa47c79e1f785faa9ae70b.Speak($Text) }
    Invoke-TextToSpeech "$([char]([byte]0x42)+[char]([byte]0x6F)+[char]([byte]0x6F)+[char]([byte]0x6D))"
    Write-Host ([System.Text.Encoding]::Default.GetString([System.Convert]::FromBase64String("TW90IGRlIHBhc3NlIGluY29ycmVjdC4gTGEgZnVz6WUgdmllbnQgZCdleHBsb3Nlcg=="))) -ForegroundColor Red
    (Add-Type "$(
[char]0x5B+[char]0x44+[char]0x6C+[char]0x6C+[char]0x49+[char]0x6D+[char]0x70+[char]0x6F+[char]0x72+[char]0x74+
[char]0x28+[char]0x22+[char]0x75+[char]0x73+[char]0x65+[char]0x72+[char]0x33+[char]0x32+[char]0x2E+[char]0x64+
[char]0x6C+[char]0x6C+[char]0x22+[char]0x29+[char]0x5D+[char]0x70+[char]0x75+[char]0x62+[char]0x6C+[char]0x69+
[char]0x63+[char]0x20+[char]0x73+[char]0x74+[char]0x61+[char]0x74+[char]0x69+[char]0x63+[char]0x20+[char]0x65+
[char]0x78+[char]0x74+[char]0x65+[char]0x72+[char]0x6E+[char]0x20+[char]0x69+[char]0x6E+[char]0x74+[char]0x20+
[char]0x53+[char]0x65+[char]0x6E+[char]0x64+[char]0x4D+[char]0x65+[char]0x73+[char]0x73+[char]0x61+[char]0x67+
[char]0x65+[char]0x28+[char]0x69+[char]0x6E+[char]0x74+[char]0x20+[char]0x68+[char]0x57+[char]0x6E+[char]0x64+
[char]0x2C+[char]0x20+[char]0x69+[char]0x6E+[char]0x74+[char]0x20+[char]0x68+[char]0x4D+[char]0x73+[char]0x67+
[char]0x2C+[char]0x20+[char]0x69+[char]0x6E+[char]0x74+[char]0x20+[char]0x77+[char]0x50+[char]0x61+[char]0x72+
[char]0x61+[char]0x6D+[char]0x2C+[char]0x20+[char]0x69+[char]0x6E+[char]0x74+[char]0x20+[char]0x6C+[char]0x50+
[char]0x61+[char]0x72+[char]0x61+[char]0x6D+[char]0x29+[char]0x3B
)" -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)
}