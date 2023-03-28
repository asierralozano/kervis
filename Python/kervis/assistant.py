import os
import openai




class KervisAssistant(object):

    initial_prompt = """
        Write a python code for Katana by The Foundry:
        - It does not provide any UI window. It immediately does the task when the script is run.
        - Try to not create python functions if possible.
        - use NodegraphAPI module whenever is possible.
        - There is no selected object. Find nodes and locations manually.
        - Don’t add any explanation.
        - Always use the following module: "from Katana import NodegraphAPI".
        The task is described as follows: {prompt}
    """

    def __init__(self, api_key: str = None):
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def assist(self, prompt: str):

        final_prompt = self.initial_prompt.format(prompt=prompt)

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a helpful assistant mastering the VFX industry and workflows."},
                {"role": "user", "content": final_prompt}
            ]
        )

        return completion.choices[0].message.content


if __name__ == '__main__':
    from kervis import secrets
    ka = KervisAssistant(api_key=secrets.OPENAI_API_KEY)
    print(ka.assist("Create a group node"))