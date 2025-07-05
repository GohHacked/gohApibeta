import g4f

class GPTClient:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def chat(self, messages):
        """
        messages - список словарей, например [{"role": "user", "content": "Привет"}]
        Возвращает - {"response": "текст ответа"}
        """
        try:
            response = g4f.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            return {"response": response}
        except Exception as e:
            raise RuntimeError(f"Ошибка в g4f: {e}")