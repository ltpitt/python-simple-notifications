from click.testing import CliRunner
import simple_notifications

def test_help():
    runner = CliRunner()
    result = runner.invoke(simple_notifications.pushover)
    assert result.exit_code == 0
    assert "Usage: simple-notifications" in result.output



# @pytest.fixture
# def runner():
#     return CliRunner()
#
#
# def test_cli(runner):
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert not result.exception
#     assert 'Usage: simple-notifications' in result.output.strip()


# def test_cli_with_option(runner):
#    result = runner.invoke(cli.main, ['--as-cowboy'])
#    assert not result.exception
#    assert result.exit_code == 0
#    assert result.output.strip() == 'Howdy, world.'
#
#
# def test_cli_with_arg(runner):
#    result = runner.invoke(cli.main, ['Davide'])
#    assert result.exit_code == 0
#    assert not result.exception
#    assert result.output.strip() == 'Hello, Davide.'
