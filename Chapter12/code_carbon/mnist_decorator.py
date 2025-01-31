"""
This sample code sis taken from https://github.com/mlco2/codecarbon/blob/master/examples/
It shows how to use CodeCarbon by using it asa decorator in the Keras training function
It helps to compute the emissions in the overall training process
"""


import tensorflow as tf

from codecarbon import track_emissions


@track_emissions(project_name="mnist")
def train_model():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10),
        ]
    )
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

    model.fit(x_train, y_train, epochs=10)
    return model


if __name__ == "__main__":
    model = train_model()
