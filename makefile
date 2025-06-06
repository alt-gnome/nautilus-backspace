PREFIX      ?= /usr
DATAROOTDIR ?= $(PREFIX)/share

ifeq ($(shell id -u), 0)
	INSTALL_DATAROOTDIR := $(DATAROOTDIR)
else
	INSTALL_DATAROOTDIR := $(HOME)/.local/share
endif

EXTENSION_DIR := $(INSTALL_DATAROOTDIR)/nautilus-python/extensions
SCHEMA_DIR    := $(INSTALL_DATAROOTDIR)/glib-2.0/schemas

INSTALL      := install
INSTALL_DATA := $(INSTALL) -m0644

SCRIPT := Back.py
SCHEMA := io.github.alt-gnome-team.nautilus-backspace.gschema.xml

.PHONY: all install schemas

all:
	@echo "Available targets: install, schemas"

install: $(SCRIPT) $(SCHEMA)
	$(INSTALL) -d $(EXTENSION_DIR)
	$(INSTALL_DATA) $(SCRIPT) $(EXTENSION_DIR)

	$(INSTALL) -d $(SCHEMA_DIR)
	$(INSTALL_DATA) $(SCHEMA) $(SCHEMA_DIR)/$(SCHEMA)

schemas:
	glib-compile-schemas $(SCHEMA_DIR)
