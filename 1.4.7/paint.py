from keras.models import Model, Sequential, load_model
from keras.layers import Input, Dense, Conv2D, Conv2DTranspose, BatchNormalization, Activation, Flatten, Dropout
from keras.layers.advanced_activations import LeakyReLU
from keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img, save_img
import numpy as np

image_shape = (100, 100, 3)

class Classify():
    def __init__(self):
        self.model = Sequential()

        self.model.add(Conv2D(
            filters=32,
            kernel_size=(3, 3),
            input_shape=image_shape,
            data_format="channels_last"
        ))
        self.model.add(LeakyReLU(alpha=0.2))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(
            filters=64,
            kernel_size=(3, 3),
            input_shape=image_shape,
            data_format="channels_last"
        ))
        self.model.add(BatchNormalization(momentum=0.8))
        self.model.add(LeakyReLU(alpha=0.2))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(
            filters=128,
            kernel_size=(3, 3),
            input_shape=image_shape,
            data_format="channels_last"
        ))
        self.model.add(BatchNormalization(momentum=0.8))
        self.model.add(LeakyReLU(alpha=0.2))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(
            filters=256,
            kernel_size=(3, 3),
            input_shape=image_shape,
            data_format="channels_last"
        ))
        self.model.add(BatchNormalization(momentum=0.8))
        self.model.add(LeakyReLU(alpha=0.2))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(1))
        self.model.add(Activation("sigmoid"))

        x = Input(shape=image_shape)
        y = self.model(x)
        self.model = Model(x, y)
        self.model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    def train(self):
        data_generator = ImageDataGenerator(
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True
        )
        self.model.fit_generator(
            data_generator.flow_from_directory(
                "data",
                target_size=image_shape[:2],
                classes=["images", "paintings"],
                batch_size=32,
                class_mode="binary"
            ),
            steps_per_epoch=64,
            epochs=3
        )

class Paint():
    def __init__(self, classify):
        self.classify = classify
        self.model = Sequential()

        self.model.add(Conv2D(
            filters=32,
            kernel_size=(3, 3),
            input_shape=image_shape,
            data_format="channels_last"
        ))
        self.model.add(Activation("relu"))

        self.model.add(Conv2D(
            filters=64,
            kernel_size=(3, 3)
        ))
        self.model.add(BatchNormalization(momentum=0.8))
        self.model.add(Activation("relu"))

        self.model.add(Conv2D(
            filters=128,
            kernel_size=(3, 3)
        ))
        self.model.add(BatchNormalization(momentum=0.8))
        self.model.add(Activation("relu"))

        self.model.add(Conv2DTranspose(
            filters=64,
            kernel_size=(3, 3)
        ))
        self.model.add(BatchNormalization(momentum=0.8))
        self.model.add(Activation("relu"))

        self.model.add(Conv2DTranspose(
            filters=3,
            kernel_size=(3, 3)
        ))
        self.model.add(Activation("tanh"))

        x = Input(shape=image_shape)
        y = self.model(x)
        self.model = Model(x, y)

        x_c = Input(shape=image_shape)
        y_c = self.model(x_c)
        z_c = self.classify.model(y_c)
        self.combined = Model(x_c, z_c)
        self.combined.compile(loss="binary_crossentropy", optimizer="adam")

    def loss(self, y_true, y_pred):
        loss_y_pred = y_pred
        print("SHAPE", y_pred.shape)

        for layer in [layer for layer in self.classify.model.layers]:
            loss_y_pred = layer(loss_y_pred)

        return -loss_y_pred + 1.0


class Painting():
    def __init__(self):
        self.classify = Classify()
        self.paint = Paint(self.classify)

    def load(self):
        self.classify.model = load_model("model/classify.h5")
        self.paint.model = load_model("model/paint.h5")

    def train(self):
        image_generator = ImageDataGenerator().flow_from_directory(
            "data",
            target_size=image_shape[:2],
            classes=["images"],
            batch_size=32,
            class_mode=None
        )

        painting_generator = ImageDataGenerator(
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True
        ).flow_from_directory(
            "data",
            target_size=image_shape[:2],
            classes=["paintings"],
            batch_size=32,
            class_mode=None
        )

        real = np.ones(32, dtype=float)
        fake = np.zeros(32, dtype=float)
        batch = 0

        for image_batch, painting_batch in zip(image_generator, painting_generator):
            batch += 1

            if image_generator.total_batches_seen == 3 * len(image_batch):
                break
            elif image_batch.shape[0] != 32 or painting_batch.shape[0] != 32:
                continue
            else:
                if batch % 3 == 0:
                    self.run()

                fake_painting_batch = self.paint.model.predict(image_batch)

                classify_loss_real = self.classify.model.train_on_batch(painting_batch, real)
                classify_loss_fake = self.classify.model.train_on_batch(fake_painting_batch, fake)
                classify_loss = 0.5 * np.add(classify_loss_real, classify_loss_fake)

                paint_loss = self.paint.combined.train_on_batch(image_batch, real)

                print("Batch(%d) Classify-Loss(%.2f) Classify-Accuracy(%.2f%%) Paint-Loss(%.3f)" % (batch, classify_loss[0], 100.0 * classify_loss[1], paint_loss))

        self.classify.model.save("model/classify.h5")
        self.paint.model.save("model/paint.h5")

    def run(self):
        save_img("painting.jpg", array_to_img(self.paint.model.predict(np.array([img_to_array(load_img("data/images/42102_73212f0ee4.jpg", target_size=image_shape[:2]))]))[0]))

painting = Painting()
#painting.load()
painting.train()