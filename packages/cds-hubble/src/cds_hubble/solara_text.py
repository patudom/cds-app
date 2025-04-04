import solara
from solara.alias import rv


@solara.component
def TestComponent(input_text: solara.Reactive[str]):
    with rv.Card(width=400) as main:
        print("Internal re-render.")

        rv.TextField(v_model=input_text.value, on_v_model=input_text.set)

        with rv.CardText():
            solara.Text(f"You typed: {input_text.value}")

    return main


@solara.component
def Page():
    counter = solara.use_reactive(0)
    input_text = solara.use_reactive("Write something!")

    with rv.Container():
        with rv.Row():
            with rv.Col():
                print("External re-render.")
                solara.Text(f"Button counter: {counter.value}")
                solara.Button("Click me!", on_click=lambda: counter.set(counter.value + 1))

        with rv.Row():
            with rv.Col():
                def _some_callback():
                    TestComponent(input_text)

                _some_callback()