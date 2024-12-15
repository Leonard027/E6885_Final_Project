import tensorflow as tf
from tensorflow.keras import layers, models

class PolicyValueNet:
    def __init__(self, board_size):
        self.board_size = board_size
        self.model = self._build_model()

    def _build_model(self):
        input_layer = layers.Input(shape=(self.board_size, self.board_size, 2))
        x = layers.Conv2D(64, kernel_size=3, padding="same", activation="relu")(input_layer)
        x = layers.Conv2D(64, kernel_size=3, padding="same", activation="relu")(x)
        x = layers.Flatten()(x)
        policy_head = layers.Dense(self.board_size**2, activation="softmax", name="policy")(x)
        value_head = layers.Dense(1, activation="tanh", name="value")(x)

        model = models.Model(inputs=input_layer, outputs=[policy_head, value_head])
        model.compile(optimizer="adam",
                      loss={"policy": "categorical_crossentropy", "value": "mse"})
        return model

    def predict(self, state):
        return self.model(state)