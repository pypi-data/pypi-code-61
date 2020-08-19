import logging

import click

from fefu_admission.fefu import FefuUniversity, FefuSettings
from fefu_admission.university.university.printer import UniversityInformationPrinter
from fefu_admission.university.applicants_holder.printer import ApplicantsHolderInformationPrinter
from fefu_admission.utils import Utils

fefu = FefuUniversity(settings=FefuSettings)

logging.basicConfig(level=logging.INFO)


class ChoiceOption(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)
        if not isinstance(self.type, click.Choice):
            raise Exception('ChoiceOption type arg must be click.Choice')

        if self.prompt:
            prompt_text = '{}:\n{}\n'.format(
                self.prompt,
                '\n'.join(f'{idx: >4}: {c}' for idx, c in enumerate(self.type.choices, start=1))
            )
            self.prompt = prompt_text

    def process_prompt_value(self, ctx, value, prompt_type):
        if value is not None:
            index = prompt_type(value, self, ctx)
            return self.type.choices[index - 1]

    def prompt_for_value(self, ctx):
        # Calculate the default before prompting anything to be stable.
        default = self.get_default(ctx)

        prompt_type = click.IntRange(min=1, max=len(self.type.choices))
        return click.prompt(
            self.prompt, default=default, type=prompt_type,
            hide_input=self.hide_input, show_choices=False,
            confirmation_prompt=self.confirmation_prompt,
            value_proc=lambda x: self.process_prompt_value(ctx, x, prompt_type))


@click.group()
def cli():
    pass


@cli.command("load", help="Load data from website and save to ~/.fefu_admission/data/")
def load():
    global fefu
    fefu.load_from_web_all()
    fefu.serialization.save_data_to_file_all()


@cli.command("search_matches", help="Shows matches in a row")
@click.option('--date', default=None, required=False)
def search_matches(date):
    global fefu
    fefu.serialization.load_from_file_all(Utils.get_date(date))
    fefu.processing_all_departments()
    UniversityInformationPrinter(fefu).search_for_matches()


@cli.command("stats", help="Get statistics of the competitive situation")
@click.option('--date', default=None, required=False)
def show_stats(date):
    global fefu
    fefu.serialization.load_from_file_all(Utils.get_date(date))
    fefu.processing_all_departments()
    UniversityInformationPrinter(fefu).print_info()
    for dep in fefu.departments:
        ApplicantsHolderInformationPrinter(dep).print_info()


@cli.command("list", help="Show list of any department")
@click.option('--department', prompt='Index of department', help='Index of department',
              type=click.Choice([x for x in fefu.departments], case_sensitive=False), cls=ChoiceOption)
@click.option('--agreement', is_flag=True)
@click.option('--date', default=None, required=False)
def show_list(department, agreement, date):
    global fefu
    fefu.serialization.load_from_file_all(Utils.get_date(date))
    UniversityInformationPrinter(fefu).print_list_of_department(department, agreement)


if __name__ == '__main__':
    cli()
