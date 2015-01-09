from vint.ast.node_type import NodeType
from vint.linting.level import Level
from vint.linting.policy.abstract_policy import AbstractPolicy
from vint.linting.policy_registry import register_policy
from vint.ast.plugin.scope_plugin import ExplicityOfScopeVisibility


@register_policy
class ProhibitImplicitScopeVariable(AbstractPolicy):
    def __init__(self):
        super(ProhibitImplicitScopeVariable, self).__init__()
        self.reference = 'Anti-pattern of vimrc (Scope of variable)'
        self.level = Level.WARNING


    def listen_node_types(self):
        return [NodeType.IDENTIFIER]


    def is_valid(self, identifier, lint_context):
        """ Whether the identifier has a scope prefix. """

        scope_plugin = lint_context['plugins']['scope']
        explicity = scope_plugin.get_explicity_of_scope_visibility(identifier)

        self._make_description(identifier, scope_plugin)

        return explicity is not ExplicityOfScopeVisibility.IMPLICIT


    def _make_description(self, identifier, scope_plugin):
        self.description = 'Make the scope explicit like `{good_example}`'.format(
            good_example=scope_plugin.normalize_variable_name(identifier)
        )