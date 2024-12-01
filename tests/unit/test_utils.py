from orkestr8.utils import build_training_data_response


class TestUtils:
    def test_parse_training_data(self):
        # ARRANGE
        epoch = 1
        accuracy_hist_train = 0.50
        accuracy_hist_valid = 0.40
        end = 0.2890
        loss_hist_train = 1.850
        loss_hist_valid = 1.4
        dir_name = "test"

        text = (
            f"[Data-row] {epoch=}, train_acc={accuracy_hist_train*100:.2f}%, "
            + f"test_acc={accuracy_hist_valid*100:.2f}%, time={end:.2f}sec, "
            + f"train_loss={loss_hist_train:.4f}, val_loss={loss_hist_valid:.4f}, {dir_name=}"
        )

        # ACT
        result = build_training_data_response(text)

        assert {
            "epoch": 1,
            "train_acc": "50.00%",
            "test_acc": "40.00%",
            "time": "0.29sec",
            "train_loss": 1.850,
            "val_loss": 1.4,
            "dir_name": "'test'",
        } == result
