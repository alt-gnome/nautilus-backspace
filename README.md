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

### 2. Устанавливаем расширение.

```shell
curl -sSL https://raw.githubusercontent.com/alt-gnome-team/nautilus_backspace/main/install | sh
```

## Настройка

### Меняем сочетание:

Открываем config
```shell
nano ~/.config/nautilus_backspace/config
```

Вставляем необходимое сочетание
```ini
[DEFAULT]
shortcut = <Alt>Down
```