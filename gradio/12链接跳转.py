# DEV reloads require a refresh on the browser.
import gradio as gr

session_states = {}


#
# PAGES can be in external files
#
def get_not_found_page(local_state):
    with gr.Column() as result:
        gr.Markdown("## 404 - PAGE NOT FOUND")

        gr.Label(f"404 Page {type(local_state)}: {local_state.get('page')}")
    return result


def get_landing_page(local_state):
    with gr.Column() as result:
        gr.Markdown("## LANDING PAGE")

        if local_state:
            gr.Label(f"Landing Page {type(local_state)}")
            gr.Label(f"Page: {local_state.get('page')}")
    return result


def get_home_page(local_state):
    with gr.Column() as result:
        gr.Markdown("## Home")

        gr.Label(f"Home Page {type(local_state)}")
        gr.Label(f"Page: {local_state.get('page')}")
    return result


def get_faq_page(local_state):
    with gr.Column() as result:
        gr.Markdown("## FAQ")

        gr.Label(f"FAQ Page {type(local_state)}")
        gr.Label(f"Page: {local_state.get('page')}")
    return result


#
# APP_SHELL - for multiple pages
#
with gr.Blocks() as demo:
    def init_state(request: gr.Request):

        # TODO: ADD SECURITY/PERSISTENCE HERE
        session_id = "123"
        if request and "session" in request.cookies:
            session_id = request.cookies["session"]
            print(f"** session_id: {session_id}")
            if session_id not in session_states:
                session_states[session_id] = {
                    "user": "jdoe123",
                    "session_id": session_id,
                    "tasks": [],
                    "page": "",
                }
        result = session_states[session_id]

        #
        # PULL URL PARAMS HERE
        #
        result["page"] = request.query_params.get("page")
        return result  # this result populates "state"


    state = gr.State()

    #
    # POPULATE user "state" with request data
    #
    demo.load(
        fn=init_state,
        inputs=None,
        outputs=state,
        queue=True,
        show_progress=False,
    )

    content = gr.HTML("...")


    @gr.render(inputs=[state], triggers=[state.change])
    def page_content(local_state):
        with gr.Row(variant="panel") as result:
            with gr.Column(scale=0, min_width=50):
                anchor = gr.HTML("<h1>🏠</h1>")

                #
                # BUTTONS FOR PAGE NAVIGATION
                #
                with gr.Column() as result:
                    gr.Button("👥", link="/")
                    gr.Button("🏠", link="/?page=home")
                    gr.Button("💼", link="/?page=faq")

            with gr.Column(scale=12):
                #
                # SIMPLE PAGE ROUTING HERE
                #
                if (
                        local_state == None
                        or local_state["page"] == None
                        or len(local_state["page"]) < 1
                ):
                    return get_landing_page(local_state), local_state
                elif local_state["page"] == "home":
                    return get_home_page(local_state), local_state
                elif local_state["page"] == "faq":
                    return get_faq_page(local_state), local_state
                else:
                    return (
                        get_not_found_page(local_state),
                        local_state,
                    )


    #
    # HACK: Would be nice to delay rendering until state is populated
    #
    def page_content_update(local_state):
        return gr.HTML("...", visible=False)


    state.change(fn=page_content_update, inputs=state, outputs=content)

demo.launch()
