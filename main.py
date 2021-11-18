import traceback
from modules.Base import checkLotto
from modules.LineNotify import LineNotify

if __name__ == "__main__":
    try:
        checkLotto()
    except Exception as e:
        trace = traceback.print_exc()
        LineNotify().sendMessage(f"บอทกำลังมีปัญหา เกิด error ขึ้นดังนี้ : {str(trace)}")

