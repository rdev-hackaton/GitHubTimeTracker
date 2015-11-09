from click.core import Option, Parameter


class DependentOption(Option):
    """
    Option dependent in someway on another option
    """

    def __init__(self, *args, **kwargs):
        """
        You can specify prompt_depends_on key word argument.
        It should be tuple with name of option and boolean.
        True means that prompt is only needed if option on which
        this one depends is present and not None, False the opposite.
        """
        self.prompt_depends_on = kwargs.pop('prompt_depends_on')
        if not isinstance(self.prompt_depends_on, tuple):
            raise TypeError("prompt_depends_on should be a tuple")
        super().__init__(*args, **kwargs)

    def _check_prompt_dependency(self, ctx):
        option, present = self.prompt_depends_on
        return bool(ctx.params.get(option, None)) == present

    def full_process_value(self, ctx, value):
        if value is None and self.prompt is not None \
                and not ctx.resilient_parsing \
                and self._check_prompt_dependency(ctx):
            return self.prompt_for_value(ctx)
        return Parameter.full_process_value(self, ctx, value)
