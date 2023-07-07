# Loop runs endlessly
# Sometimes `mkdocs serve` crashes when moving files while it's building

while($true)
{
    # & "mkdocs serve";
    cmd.exe /c "mkdocs serve";
    Start-Sleep -Seconds 1.5;
}