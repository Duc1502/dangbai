# Intercept /dang-bai slash command and run the skill

# Read from stdin (hook passes JSON)
$input = Read-Host
$json = $input | ConvertFrom-Json -ErrorAction SilentlyContinue

if ($json -and $json.prompt) {
    $prompt = $json.prompt

    # Check if prompt starts with /dang-bai
    if ($prompt -like "/dang-bai*") {
        # Get the project root
        $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
        $projectRoot = Split-Path -Parent (Split-Path -Parent $scriptDir)

        # Run the skill
        Push-Location $projectRoot
        try {
            & python .\.claude\skills\dang-bai\main.py
        }
        finally {
            Pop-Location
        }

        # Return continue: false to prevent submission
        $result = @{ continue = $false; systemMessage = "Running /dang-bai skill..." } | ConvertTo-Json
        Write-Output $result
        exit 0
    }
}

# Allow other prompts to be submitted normally
exit 0
