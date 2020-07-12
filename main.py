#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:29:47 2020

@author: Nelson
"""

import sys
from pymatgen import MPRester
from pymatgen.io.pwscf import PWInput

if __name__ == '__main__':
    mpid = sys.argv[2]
    with MPRester(sys.argv[1]) as m:
        mpStruct = m.get_structure_by_material_id(mpid)
    
    # Pseudo setup
    Pseudos = {}
    for iatm in mpStruct.species:
        Pseudos[iatm.value] = iatm.value + '.xyz.UPF'
                    
    scfIn = PWInput(structure=mpStruct, pseudo=Pseudos)

    fname = mpid + '.scf.in'    
    scfIn.write_file(fname)
