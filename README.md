# nautilus backspace

> [!NOTE]
> Идея принадлежит [riclc](https://github.com/riclc), увы, но автор забросил свой аккаунт.


Расширение позволяет возвращаться в предыдущую директорию в Nautilus по нажатию кнопки backspace

## Установка

### 1. Устанавливаем зависимости.

#### Debian/Ubuntu

```shell
sudo apt-get install python-nautilus
```

#### ALT Linux

```shell
su -
apt-get update
apt-get install nautilus-python libnautilus-gir
```
Или через epm:

```shell
epm -i nautilus-python libnautilus-gir
```
### 2. Создаём директорию для расширений.

```shell
mkdir -p ~/.local/share/nautilus-python/extensions/
```

### 3. Устанавливаем расширение.

```shell
wget -P ~/.local/share/nautilus-python/extensions/ https://raw.githubusercontent.com/fiersik/nautilus_backspace/main/Back.py
```