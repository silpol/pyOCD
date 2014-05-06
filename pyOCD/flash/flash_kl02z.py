"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4931b510, 0x60082000, 0x44484830, 0xf896f000, 0xd0002800, 0xbd102001, 0x47702000, 0xb510482b, 
    0xf0004448, 0x0004f87d, 0x4828d105, 0x44482100, 0xf914f000, 0xf0004604, 0x2c00f83f, 0x2001d001, 
    0x2000bd10, 0xb570bd10, 0x46014605, 0x2201481f, 0xf0004448, 0x0004f83f, 0x481cd107, 0x22012300, 
    0x44484629, 0xf8c2f000, 0xf0004604, 0x2c00f825, 0x2001d001, 0x2000bd70, 0xb5febd70, 0x460b460d, 
    0x46014607, 0x46164811, 0xf0004448, 0x0004f88b, 0x9000d10a, 0x90029001, 0x4633480c, 0x4639462a, 
    0xf0004448, 0x4604f8e9, 0xf806f000, 0xd0012c00, 0xbdfe2001, 0xbdfe2000, 0x68c14805, 0x02922201, 
    0x60c14311, 0x00004770, 0x40048100, 0x00000004, 0xf0003000, 0x4614b5f8, 0xf000460d, 0x2800f848, 
    0x192cd118, 0x05a11e64, 0x0aa1d003, 0x028c1c49, 0x4e091e64, 0x2709447e, 0xd80b42a5, 0x60056830, 
    0x71c74806, 0xf8e8f000, 0xd1032800, 0x02892101, 0xe7f1186d, 0x0000bdf8, 0x0000038c, 0x40020000, 
    0x2800b510, 0x4904d005, 0x71c82044, 0xf8d4f000, 0x2004bd10, 0x0000bd10, 0x40020000, 0xd0122800, 
    0x68c94916, 0x01094a16, 0x00490f09, 0x5a51447a, 0xd00a0309, 0x60022200, 0x21016041, 0x02896081, 
    0x461060c1, 0x20044770, 0x20644770, 0x28004770, 0x460bd005, 0x079b4313, 0x2065d003, 0x20044770, 
    0x68034770, 0xd804428b, 0x18896840, 0x42881818, 0x2066d201, 0x20004770, 0x00004770, 0x40048040, 
    0x00000312, 0x461db5f8, 0x460e0014, 0x461ad017, 0xffddf7ff, 0xd1132800, 0x447f4f0a, 0xd00f2d00, 
    0x60066838, 0x6839cc01, 0x49076048, 0x71c82006, 0xf882f000, 0xd1032800, 0x1f2d1d36, 0x2004e7ee, 
    0x0000bdf8, 0x000002c6, 0x40020000, 0xb081b5ff, 0x460e4614, 0xf7ff4605, 0x2800ffba, 0x68a9d127, 
    0xf0006868, 0x9000f881, 0x42404271, 0x424d4001, 0xd10142b5, 0x182d9800, 0xd0172c00, 0x42a71baf, 
    0x4627d900, 0x08b9480b, 0x68004478, 0x480a6006, 0x71c22201, 0x72c20a0a, 0x99047281, 0xf0007241, 
    0x2800f84b, 0x1be4d103, 0xe7e319f6, 0xb0052000, 0x0000bdf0, 0x00000258, 0x40020000, 0x2800b510, 
    0x4804d006, 0x71c22240, 0xf0007181, 0xbd10f835, 0xbd102004, 0x40020000, 0x9f08b5f8, 0x4616001c, 
    0xd004460d, 0xff73f7ff, 0xd1012800, 0x2004e01d, 0x480fbdf8, 0x68014478, 0x490e600d, 0x71ca2202, 
    0x72ca9a06, 0x68216800, 0xf0006081, 0x2800f815, 0x9907d008, 0xd0002900, 0x2f00600d, 0x2100d0e8, 
    0xbdf86039, 0x1d241f36, 0x2e001d2d, 0xbdf8d1e1, 0x000001ec, 0x40020000, 0x2170480a, 0x21807001, 
    0x78017001, 0xd0fc09c9, 0x06817800, 0x2067d501, 0x06c14770, 0x2068d501, 0x07c04770, 0x2069d0fc, 
    0x00004770, 0x40020000, 0x09032200, 0xd32c428b, 0x428b0a03, 0x2300d311, 0xe04e469c, 0x430b4603, 
    0x2200d43c, 0x428b0843, 0x0903d331, 0xd31c428b, 0x428b0a03, 0x4694d301, 0x09c3e03f, 0xd301428b, 
    0x1ac001cb, 0x09834152, 0xd301428b, 0x1ac0018b, 0x09434152, 0xd301428b, 0x1ac0014b, 0x09034152, 
    0xd301428b, 0x1ac0010b, 0x08c34152, 0xd301428b, 0x1ac000cb, 0x08834152, 0xd301428b, 0x1ac0008b, 
    0x08434152, 0xd301428b, 0x1ac0004b, 0x1a414152, 0x4601d200, 0x46104152, 0xe05d4770, 0xd0000fca, 
    0x10034249, 0x4240d300, 0x22004053, 0x0903469c, 0xd32d428b, 0x428b0a03, 0x22fcd312, 0xba120189, 
    0x428b0a03, 0x0189d30c, 0x428b1192, 0x0189d308, 0x428b1192, 0x0189d304, 0x1192d03a, 0x0989e000, 
    0x428b09c3, 0x01cbd301, 0x41521ac0, 0x428b0983, 0x018bd301, 0x41521ac0, 0x428b0943, 0x014bd301, 
    0x41521ac0, 0x428b0903, 0x010bd301, 0x41521ac0, 0x428b08c3, 0x00cbd301, 0x41521ac0, 0x428b0883, 
    0x008bd301, 0x41521ac0, 0x0843d2d9, 0xd301428b, 0x1ac0004b, 0x1a414152, 0x4601d200, 0x41524663, 
    0x4610105b, 0x4240d301, 0xd5002b00, 0x47704249, 0x105b4663, 0x4240d300, 0x2000b501, 0x46c046c0, 
    0x0002bd02, 0x00000004, 0x00000008, 0x00000010, 0x00000020, 0x00000040, 0x00000000, 0x00000000, 
    0x00000020, 0x40020004, 0x00000000, 
                                ],
               'pc_init' : 0x20000021,
               'pc_eraseAll' : 0x2000003D,
               'pc_erase_sector' : 0x20000067,
               'pc_program_page' : 0x2000009B,
               'begin_stack' : 0x20000800,
               'begin_data' : 0x20000a00,
               'static_base' : 0x20000000 + 0x20 + 0x488,
               'page_size' : 1024
              };

class Flash_kl02z(Flash):
    
    def __init__(self, target):
        super(Flash_kl02z, self).__init__(target, flash_algo)
    
