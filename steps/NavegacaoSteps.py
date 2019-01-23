@given(u'Acessar pagina inicial')
def step_impl(context):
    pass


@when(u'Clicar no icone da pagina de projetos')
def step_impl(context):
    context.homePage.clicar_item_menu()


@then(u'A pagina de projeto abre')
def step_impl(context):
    pass