<h1 align="center">
    Nautilus backspace
</h1>

<p align="center">
  Расширения для возврата назад в Nautilus по нажатию сочетания клавиш, назначенного через GSettings
</p>


> [!NOTE]
> Идея принадлежит [riclc](https://github.com/riclc), но, увы, автор забросил свой аккаунт.


Расширение позволяет возвращаться в предыдущую директорию в Nautilus по нажатию кнопки backspace или иного сочетания клавиш, назначенного через файл конфигурации.

## Установка из репозитория

[![Packaging status](https://repology.org/badge/vertical-allrepos/nautilus-backspace.svg)](https://repology.org/project/nautilus-backspace/versions)

### ALT Sisyphus
```shell
su -
apt-get update
apt-get install nautilus-backspace
```


## Сборка из исходного кода

```shell
git clone https://github.com/alt-gnome-team/nautilus-backspace.git
cd nautilus-backspace
```

### Зависимости

#### ALT Sisyphus
```shell
su -
apt-get update
apt-get install nautilus-python libnautilus-gir
```

#### Fedora
```shell
sudo dnf update
sudo dnf install nautilus-python
```

#### Debian/Ubuntu
```shell
sudo apt update
sudo apt install python3-nautilus gir1.2-nautilus-4.0
```

### Сборка

#### Системная установка
```
sudo make
sudo make schemas 
```

#### Пользовательская установка
```
make
make schemas 
```


## Настройка

### Меняем сочетание:
```shell
gsettings set io.github.alt-gnome-team.nautilus-backspace back '<Alt>Down'
```