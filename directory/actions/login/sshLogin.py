#此文件用于接受用户输入的账号密码
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSSHLogin(Action):
    def name(self) -> Text:
        return "action_ssh_login"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)
        user = tracker.slots.get("user")
        password = tracker.slots.get("password")
        msg = f"获取到的账号密码是{user}/{password}"
        dispatcher.utter_message(text=msg)