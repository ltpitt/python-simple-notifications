from click.testing import CliRunner
from simple_notifications import cli


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli.notification)
    assert result.exit_code == 0
    assert "Usage: " in result.output
