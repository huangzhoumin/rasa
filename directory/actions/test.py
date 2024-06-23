from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionGreetUser(Action):
    def name(self):
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        # 获取用户的名字（假设已经通过其他操作设置了名字这个slot）
        user_name = tracker.get_slot('name') or "there"
        # 向用户发出欢迎
        dispatcher.utter_message(f"Hello {user_name}! How are you today?")
        # 返回一个事件列表，这里我们不需要其他事件，所以返回空列表
        return []