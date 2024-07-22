# SimpleUEFI:

### Reason:
Well, i found the installation and usage of the EDK2 extemely tedious,
then i discovered [VisualUEFI](https://github.com/ionescu007/VisualUefi)
which implements the EDK2 into visual studio but still i wasn't quite satisfied
since i tend to reinstall windows really often i coded a little script in python
(yh, not in batch cuz i was lazy) that sets up some presets on VisualStudio with which 
you can create `UEFI applications`/`Dxe Drivers`/`UEFI Drivers` projects.

### Credits:
- [VisualUEFI](https://github.com/ionescu007/VisualUefi) By: [ionescu007](https://github.com/ionescu007)
- [EDK2](https://github.com/tianocore/edk2) By: [TianoCore](https://github.com/tianocore)

### Requirements:
- [x] [NASM](https://www.nasm.us/) (Netwide Assembler)
- [x] [Python](https://www.python.org/)
- [x] [GIT](https://git-scm.com/downloads) (For submodules)
- [x] [Visual Studio](https://visualstudio.microsoft.com/downloads/) (Versions: 2015/2019/2022 Supported)

### Usage:
1. Install all the requirements listed above.
2. Clone the repo using the following command `git clone https://github.com/Th3Spl/SimpleUEFI --recursive`
3. Use the command line `python Setup.py`
4. The python file will automatically move all the needed files
5. Once the program stops it will open a folder
6. Open `EDK-II.sln` with VisualStudio and compile `(x64 Release)`
7. Once you compiled `EDK-II.sln` click any keybind on the terminal
8. The program will automatically copy the presets in the VisualStudio templates folder
9. Open VisualStudio and search for either `Uefi Application`/`Dxe Driver`/`Uefi Driver`
10. Create a new project using a preset and if everything worked it should compile without issues.

#### TODO:
- [ ] Add qemu debugging options to presets (Partially added).

##### Ps:
If you encounter any issue feel free to contact me.
- Th3Spl
