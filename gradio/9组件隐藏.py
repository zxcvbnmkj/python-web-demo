import gradio as gr
with gr.Blocks() as demo:
    # 出错提示框
    #visible=False使得应用中看不到这一个组件
    error_box = gr.Textbox(label="Error", visible=False)
    # 输入框
    name_box = gr.Textbox(label="Name")
    age_box = gr.Number(label="Age")
    #复选框
    symptoms_box = gr.CheckboxGroup(["Cough", "Fever", "Runny Nose"])
    submit_btn = gr.Button("Submit")

    # 输出不可见
    with gr.Column(visible=False) as output_col:
        diagnosis_box = gr.Textbox(label="Diagnosis")
        patient_summary_box = gr.Textbox(label="Patient Summary")

    #事件处理按钮，，写在block内部
    def submit(name, age, symptoms):
        #显示出错提示框
        if len(name) == 0:
            #gr.update用于更新组件的状态，把隐藏的组件显示出来
            return {error_box: gr.update(value="Enter name", visible=True)}
        if age < 0 or age > 200:
            return {error_box: gr.update(value="Enter valid age", visible=True)}

        #显示出隐藏的输出框
        return {
            output_col: gr.update(visible=True),
            diagnosis_box: "covid" if "Cough" in symptoms else "flu",
            patient_summary_box: f"{name}, {age} y/o"
        }

    #这种写法是错
    # def submit(name, age, symptoms):
    #     #显示出错提示框
    #     if len(name) == 0:
    #         #gr.update用于更新组件的状态，把隐藏的组件显示出来
    #         return gr.update(value="Enter name", visible=True)
    #     if age < 0 or age > 200:
    #         return gr.update(value="Enter valid age", visible=True)
    #
    #     #显示出隐藏的输出框
    #     return gr.update(value="Enter name", visible=True),gr.update(visible=True),"covid" if "Cough" in symptoms else "flu",f"{name}, {age} y/o"


    #按钮和处理函数绑定
    submit_btn.click(
        submit,
        [name_box, age_box, symptoms_box],
        [error_box, diagnosis_box, patient_summary_box, output_col],
        show_progress="full"
    )
demo.launch()