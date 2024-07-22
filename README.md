# SimpleUEFI:

### Reason:
Well, i found the installation and usage of the EDK2 extemely tedious,
then i discovered [VisualUEFI](https://github.com/ionescu007/VisualUefi)
which implements the EDK2 into visual studio but still i wasn't quite satisfied
since i tend to reinstall windows really often i coded a little script in python
(yh, not in batch cuz i was lazy) that sets up some presets on VisualStudio which 
allow to create `UEFI applications`/`Dxe Drivers`/`UEFI Drivers`.

### Credits:
- [VisualUEFI](https://github.com/ionescu007/VisualUefi) By: [ionescu007](https://github.com/ionescu007)
- [EDK2](https://github.com/tianocore/edk2) By: [TianoCore](https://github.com/tianocore)

### Requirements:
- [x] [NASM (Netwide Assembler)](https://www.nasm.us/)
- [x] [Python](https://www.python.org/)
- [x] [GIT (For submodules)](https://git-scm.com/downloads)

### Usage:
1. Install all the requirements listed above.
2. Clone the repo using the following command `git clone https://github.com/Th3Spl/SimpleUEFI --recursive`
3. Use the command line `python Setup.py`
4. The python file will automatically move all the needed files
5. Once the program stops it will open a folder
6. Open `EDK-II.sln` with VisualStudio and compile `(x64 Release)`
7. Once you compiled `EDk-II.sln` click any keybind on the terminal
8. The program will automatically copy the presets in the VisualStudio templates folder
9. Open VisualStudio and search for either `Uefi Application`/`Dxe Driver`/`Uefi Driver`
10. Create a project using one of those presets and try to compile if everything worked it should compile without issues.

### TODO:
- [ ] Add qemu debugging options (Partially added).

- Th3Spl 
