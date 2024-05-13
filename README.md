# krypton

A Python-based encryption/decryption tool with a graphical user interface (GUI) implemented using Tkinter.

## Table of Contents

- [Introduction](#introduction)
- [Algorithm](#algorithm)
- [GUI](#gui)

## Introduction

This project aims to provide a tool for encryption/decryption with an interactive GUI. The application utilizes a version of the AES-256 encryption algorithm to protect short messages. 

## Algorithm

The AES-256 encryption algorithm, more specifically the block cipher mode of operation, EAX is an AEAD algorithm which is designed to provide both authentication and privacy of the message with a two-pass scheme, one pass for achieving privacy and one for authenticity for each block. 

## GUI

The graphical user interface is implemented using Tkinter, providing users with an interactive platform to input messages that either need to be encrypted or decrypted, and then either obscure or reveal the message.

## Learn More

https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/proposed-modes/eax/eax-spec.pdf
https://en.wikipedia.org/wiki/EAX_mode



