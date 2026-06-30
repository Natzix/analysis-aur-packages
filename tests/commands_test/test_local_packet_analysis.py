from typer.testing import CliRunner

from analysis_aur.main import app

runner = CliRunner()


def test_scan_argument():
    result = runner.invoke(app, ["scan", "--analyze"])
    assert result.exit_code == 0
    assert result.stdout
