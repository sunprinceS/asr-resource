#!/usr/bin/env python3

from pathlib import Path
import json
import re
from numpy.lib.format import open_memmap
import numpy as np
import kaldiio

OUTPATH='mydata'

if __name__ == "__main__":
    cur_path = Path.cwd()    
    out_path = cur_path.joinpath(OUTPATH)
    out_path.mkdir(exist_ok=True)
    trav_ls = [(d.name,d.joinpath('deltafalse','data.json')) for d in cur_path.joinpath('dump').iterdir() if d.is_dir()]
    meta = dict()
    first = True
    regex = re.compile('[^a-zA-Z]')
    
    for name, jsf in trav_ls:
        print(f"Process {name}...")
        trim_name = regex.sub('',name)
        p = out_path.joinpath(trim_name)
        p.mkdir(exist_ok=True)
        with open(jsf, 'rb') as f:
            data = json.load(f)['utts']
            utts = list(data.keys())
            idim = int(data[utts[0]]['input'][0]['shape'][-1])
            odim = int(data[utts[0]]['output'][0]['shape'][-1])
            if not first:
                assert idim == meta['idim'] and odim == meta['odim'], "Train/Dev/Eval should have same input/output dimension"
            else:
                meta['idim'] = idim
                meta['odim'] = odim
                first = False

            #sorted by input length
            sorted_data = sorted(data.items(), key=lambda d: d[1]['input'][0]['shape'][0])

            feat_ls= list()
            ilen_ls = list()
            label_ls = list()
            olen_ls = list()

            for d in sorted_data:
                utt_name = d[0]
                feat = kaldiio.load_mat(d[1]['input'][0]['feat']) #np array
                ilen = d[1]['input'][0]['shape'][0] #int
                label = list(map(int,d[1]['output'][0]['tokenid'].split(' ')))
                olen = d[1]['output'][0]['shape'][0] #int
                assert len(label) == olen, "Label length != olen !!?"
                if olen == 0:
                    print(f"{utt_name} is 0-length")
                    continue

                feat_ls.append(feat)
                ilen_ls.append(ilen)
                label_ls.append(label)
                olen_ls.append(olen)


            feat_mat = np.vstack(feat_ls).astype('float32')
            ilen_arr = np.array(ilen_ls).astype('int')
            label_arr = np.concatenate(label_ls).astype('int')
            olen_arr = np.array(olen_ls).astype('int')


            feat_mat_data = open_memmap(out_path.joinpath(p,'feat.dat'), mode='w+', dtype='float32', shape=feat_mat.shape)
            feat_mat_data.flush()
            
            np.save(out_path.joinpath(p,'feat.npy'), feat_mat)
            np.save(out_path.joinpath(p,'ilens.npy'), ilen_arr)
            np.save(out_path.joinpath(p,'label.npy'), label_arr)
            np.save(out_path.joinpath(p,'olens.npy'), olen_arr)

            # for d in sorted_data:
                # print(d[1]['input'][0]['shape'][0])
