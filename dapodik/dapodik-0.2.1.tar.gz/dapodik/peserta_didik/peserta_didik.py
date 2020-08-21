from dataclasses import dataclass
from typing import Optional
from dapodik.base import DapodikObject
from dapodik.sekolah import Sekolah
from dapodik.rest import (JenjangPendidikan, Pekerjaan, Penghasilan,
                          KebutuhanKhusus)


@dataclass(eq=False)
class PesertaDidik(DapodikObject):
    nama: str
    jenis_kelamin: str
    tempat_lahir: str
    tanggal_lahir: str
    nama_ibu_kandung: str
    sekolah_id: Sekolah
    pdb_id: str
    tahun_lahir_ayah: int
    tahun_lahir_ibu: int
    agama_id: int
    alamat_jalan: str
    rt: int
    rw: int
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_wilayah_str: str
    kode_pos: str
    lintang: int = 0
    bujur: int = 0
    nisn: str = ""
    nik: str = ""
    tahun_lahir_wali: int = 1980
    vld_count: int = 0
    kewarganegaraan: str = "ID"
    peserta_didik_id: str = "Admin.model.PesertaDidik-1"
    kewarganegaraan_str: str = ""
    no_kk: str = ""
    reg_akta_lahir: str = ""
    agama_id_str: str = ""
    kebutuhan_khusus_id: KebutuhanKhusus = 0
    kebutuhan_khusus_id_str: str = ""
    jenis_tinggal_id: int = 1
    alat_transportasi_id: int = 1
    jenis_tinggal_id_str: str = ""
    alat_transportasi_id_str: str = ""
    no_kks: str = ""
    anak_keberapa: int = 1
    penerima_kps: int = 0
    no_kps: str = ""
    penerima_kip: int = 0
    no_kip: str = ""
    nm_kip: str = ""
    layak_pip: int = 0
    id_layak_pip: Optional[int] = None
    id_layak_pip_str: str = ""
    id_bank: str = ""
    id_bank_str: str = ""
    rekening_bank: str = ""
    nama_kcp: str = ""
    rekening_atas_nama: str = ""
    status_data: int = 0
    nama_ayah: str = ""
    nik_ayah: str = ""
    jenjang_pendidikan_ayah: JenjangPendidikan = 0
    jenjang_pendidikan_ayah_str: str = ""
    pekerjaan_id_ayah: Pekerjaan = 0
    pekerjaan_id_ayah_str: str = ""
    penghasilan_id_ayah: Penghasilan = 0
    penghasilan_id_ayah_str: str = ""
    kebutuhan_khusus_id_ayah: KebutuhanKhusus = 0
    kebutuhan_khusus_id_ayah_str: str = ""
    nik_ibu: str = ""
    jenjang_pendidikan_ibu: JenjangPendidikan = 0
    jenjang_pendidikan_ibu_str: str = ""
    pekerjaan_id_ibu: Pekerjaan = 1
    pekerjaan_id_ibu_str: str = ""
    penghasilan_id_ibu: Penghasilan = 99
    penghasilan_id_ibu_str: str = ""
    kebutuhan_khusus_id_ibu: KebutuhanKhusus = 0
    kebutuhan_khusus_id_ibu_str: str = ""
    nama_wali: str = ""
    nik_wali: str = ""
    jenjang_pendidikan_wali: JenjangPendidikan = 0
    jenjang_pendidikan_wali_str: str = ""
    pekerjaan_id_wali: Pekerjaan = 0
    pekerjaan_id_wali_str: str = ""
    penghasilan_id_wali: Penghasilan = 0
    penghasilan_id_wali_str: str = ""
    nomor_telepon_rumah: str = ""
    nomor_telepon_seluler: str = ""
    email: str = ""
    kebutuhan_khusus_id_selector = []
    kebutuhan_khusus_id_selector_ayah = []
    kebutuhan_khusus_id_selector_ibu = []
    _id: str = 'peserta_didik_id'

    @property
    def params(self):
        return {
            'sekolah_id': self.dapodik.sekolah_id,
        }
