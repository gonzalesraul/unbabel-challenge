from click.testing import CliRunner
from sam.main import main
from sam import __version__ as version


def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert result.output == 'version %s\n' % version


def test_valid_window_size():
    runner = CliRunner()
    result = runner.invoke(main, ['--window_size', '1'])
    assert result.exit_code == 0


def test_invalid_window_size():
    runner = CliRunner()
    result = runner.invoke(main, ['--window_size', '0'])
    assert result.exit_code == 2
    assert 'window_size needs to be a positive integer' in result.output


def test_valid_input():
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(main, input='{"timestamp": "2018-12-26 18:11:08.509654","event_name": "translation_delivered","duration": 20}')
    assert result.exit_code == 0


def test_invalid_input():
    runner = CliRunner()
    result = runner.invoke(main, ['-i', '/test/invalid/input'])
    assert 'Error: Invalid value for "-i" / "--input_file": Could not open file' in result.stdout
    assert result.exit_code == 2
