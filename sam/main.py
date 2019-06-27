#!/usr/bin/env python3
import sam
import click
import logging
from driftwood.formatters import JSONFormatter


# Set logging for json in case of errors will be logged to stderr in JSON format
logger = logging.getLogger("sam")
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('version {}'.format(sam.__version__))
    ctx.exit()


def positive_int(ctx, param, value):
    if value > 0:
        return value
    raise click.UsageError('%s needs to be a positive integer' % param.name)


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='Print the current version')
@click.option('-i', '--input_file', type=click.File('rb'), default='-', envvar='SAM_INPUT_FILE', help='Path to input file stream (default: stdin)')
@click.option('-w', '--window_size', type=int, default=10, callback=positive_int, envvar='SAM_WINDOW_SIZE',
                    help='Time window for the past N seconds (default: 10)\nNeeds to be a positive integer')
def main(input_file, window_size):
    pass
