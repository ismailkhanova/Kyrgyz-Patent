from django.db import models


class IpMark(models.Model):
    file_nbr = models.TextField(verbose_name='Номер')
    mark_name = models.TextField(verbose_name='Название знака')
    registration_date = models.TextField(verbose_name='Дата регистрации')
    filing_date = models.TextField(verbose_name='Дата подачи заявки')
    registration_nbr = models.TextField(verbose_name='Регистрационный номер')
    registration_dup = models.TextField(verbose_name='Регистрация_')
    expiration_date = models.TextField(verbose_name='Дата окончания')
    sign_wcode = models.TextField('Вид знака')
    owner_name = models.TextField(verbose_name='Имя владельца')
    txt_nice_class_code = models.CharField(max_length=255, verbose_name='МКТУ')

    class Meta:
        db_table = 'ip_mark'
        verbose_name = 'Товарный знак'
        verbose_name_plural = 'Товарные знаки'

    def __str__(self):
        return self.mark_name


class IpMarkNiceClasses(models.Model):
    registration_nbr = models.ForeignKey(IpMark, on_delete=models.CASCADE)
    nice_class_code = models.CharField(max_length=255)
    nice_class_description = models.TextField()

    class Meta:
        db_table = 'ip_mark_nice_classes'
        verbose_name = 'МКТУ'
        verbose_name_plural = 'МКТУ'

    def __str__(self):
        return self.nice_class_code


# ЛИЦЕНЗИОННЫЕ ДОГОВОРА
class License(models.Model):
    id_lic = models.AutoField(primary_key=True)
    id_licen = models.CharField(max_length=20)
    in_date_lic = models.TextField()
    in_number_lic = models.TextField()
    date_in_number_lic = models.CharField(max_length=256)
    ois_lic = models.TextField()
    number_lic = models.TextField()
    date_reg_lic = models.TextField()
    name_ois = models.TextField()
    licensiar = models.TextField()
    address_licensiar = models.TextField()
    licensiat = models.TextField()
    address_licensiat = models.TextField()
    dogovor_lic = models.TextField()
    prava_lic = models.TextField()
    areal_lic = models.TextField()
    date_end_lic = models.TextField()
    bulleten_lic = models.TextField()
    etc_lic = models.TextField()
    status_lic = models.IntegerField()
    person = models.CharField(max_length=20)
    date_zapis = models.TextField()

    class Meta:
        db_table = 'license'
        managed = True
        verbose_name = 'Лицензионный договор'
        verbose_name_plural = 'Лицензионные договора'

    def __str__(self):
        return self.name_ois


# АВТОРСКИЕ ПРАВА
class TblAvtor(models.Model):
    id_avtor = models.AutoField(primary_key=True)
    in_number = models.CharField(max_length=20)
    in_date = models.CharField(max_length=20, blank=True, null=True)
    regist_number = models.CharField(max_length=20)
    name_work = models.TextField()
    date_place_public = models.TextField()
    avtor = models.TextField()
    city_avtor = models.TextField()
    owner = models.TextField()
    adress_perepiski = models.TextField()
    registration_number = models.CharField(max_length=20)
    registration_date = models.TextField()
    iden = models.TextField()
    status_av = models.IntegerField()
    pseudonym = models.TextField()
    oap = models.TextField()
    date_av = models.TextField()
    num_av = models.TextField()
    etc_av = models.TextField()

    class Meta:
        db_table = 'tbl_avtor'
        managed = True
        verbose_name = 'Авторское право'
        verbose_name_plural = 'Авторские права'

    def __str__(self):
        return self.name_work


# БАЗЫ ДАННЫХ
class TblBd(models.Model):
    id_bd = models.AutoField(primary_key=True)
    in_number = models.CharField(max_length=20)
    in_date = models.CharField(max_length=128)
    number_reg = models.CharField(max_length=20)
    app_b = models.TextField()
    owner = models.TextField()
    contact = models.CharField(max_length=256)
    name = models.TextField()
    date_place_bd = models.CharField(max_length=256)
    avtor = models.TextField()
    referat = models.TextField()
    num_svid = models.CharField(max_length=20)
    date_svid = models.CharField(max_length=256)
    status_bd = models.IntegerField()

    class Meta:
        db_table = 'tbl_bd'
        managed = True
        verbose_name = 'База данных'
        verbose_name_plural = 'Авторские права'

    def __str__(self):
        return self.name


# СЕЛЕКЦИОННЫЕ ДОСТИЖЕНИЯ
class TblCel(models.Model):
    id_sel = models.AutoField(primary_key=True)
    f000 = models.TextField()
    f210 = models.TextField() #номер заявки
    f220 = models.TextField()
    f100 = models.TextField()
    f150 = models.TextField()
    f310 = models.TextField()
    f602 = models.TextField()
    f540 = models.TextField() #Название
    f570 = models.TextField()
    f600 = models.TextField()
    f601 = models.TextField()
    f980 = models.TextField()
    f731 = models.TextField()
    f732 = models.TextField()
    f733 = models.TextField()
    f941 = models.TextField()
    f149 = models.TextField()
    f450 = models.TextField()
    status_sel = models.IntegerField()

    class Meta:
        db_table = 'tbl_cel'
        managed = True
        verbose_name = 'Селекционное достижение'
        verbose_name_plural = 'Селекционные достижения'

    def __str__(self):
        return self.f540


# ЭВМ
class TblEvm(models.Model):
    id_evm = models.AutoField(primary_key=True)
    in_number = models.CharField(max_length=20)
    in_date = models.CharField(max_length=128)
    registration_number = models.CharField(max_length=20)
    app_e = models.CharField(max_length=256)
    owner = models.CharField(max_length=256)
    adress_kontact = models.CharField(max_length=256)
    name_work = models.CharField(max_length=256)
    publik_date_place = models.CharField(max_length=256)
    avtor = models.CharField(max_length=256)
    referat = models.TextField()
    number_svid = models.CharField(max_length=20)
    date_svid = models.CharField(max_length=128)
    status_evm = models.IntegerField()
    city_owner = models.TextField()
    date_evm = models.CharField(max_length=256)
    num_evm = models.CharField(max_length=256)
    etc_evm = models.TextField()

    class Meta:
        db_table = 'tbl_evm'
        managed = True
        verbose_name = 'Программа ЭВМ'
        verbose_name_plural = 'Программы ЭВМ'


# ИЗОБРЕТЕНИЯ
class TblInv(models.Model):
    id_inv = models.AutoField(primary_key=True)
    f000 = models.TextField(blank=True, null=True)
    f210 = models.TextField(blank=True, null=True)
    f220 = models.TextField(blank=True, null=True)
    f100 = models.TextField(blank=True, null=True)
    f101 = models.IntegerField()
    f150 = models.TextField(blank=True, null=True)
    f310 = models.TextField(blank=True, null=True)
    f540 = models.TextField(blank=True, null=True)
    f571 = models.TextField(blank=True, null=True)
    f572 = models.TextField(blank=True, null=True)
    f980 = models.TextField(blank=True, null=True)
    f731 = models.TextField(blank=True, null=True)
    f732 = models.TextField(blank=True, null=True)
    f733 = models.TextField(blank=True, null=True)
    f510 = models.TextField(blank=True, null=True)
    f941 = models.TextField()
    f149 = models.TextField(blank=True, null=True)
    f460 = models.TextField(blank=True, null=True)
    status_inv = models.IntegerField()

    class Meta:
        db_table = 'tbl_inv'
        managed = True
        verbose_name = 'Изобретение'
        verbose_name_plural = 'Изобретения'

    def __str__(self):
        return self.f540


#НМПТ
class TblNmpt(models.Model):
    id_nmpt = models.AutoField(primary_key=True)
    in_number = models.CharField(max_length=20)
    k11 = models.CharField(max_length=20)
    k15 = models.CharField(max_length=256)
    k18 = models.CharField(max_length=256)
    k21 = models.CharField(max_length=20)
    k22 = models.CharField(max_length=256)
    k46 = models.CharField(max_length=256)
    k54 = models.CharField(max_length=256)
    vid_tovara = models.TextField()
    k71 = models.CharField(max_length=256)
    k73 = models.TextField()
    k57 = models.TextField()
    k98 = models.TextField()
    status_nmpt = models.IntegerField()
    remark_nmpt = models.TextField()

    class Meta:
        db_table = 'tbl_nmpt'
        managed = True
        verbose_name = 'НМПТ'
        verbose_name_plural = 'НМПТ'

    def __str__(self):
        return self.k54


# ОБЩЕИЗВЕСТНЫЕ ТОВАРНЫЕ ЗНАКИ
class TblOtz(models.Model):
    id_otz = models.AutoField(primary_key=True)
    k11 = models.CharField(max_length=20)
    k15 = models.CharField(max_length=128)
    k54 = models.CharField(max_length=256)
    k73 = models.CharField(max_length=256)
    k46 = models.CharField(max_length=128)
    status_otz = models.IntegerField()
    app = models.CharField(max_length=64)

    class Meta:
        db_table = 'tbl_otz'
        managed = True
        verbose_name = 'Общеизвестный товарный знак'
        verbose_name_plural = 'Общеизвестные товарные знаки'

    def __str__(self):
        return self.k54


# ПОЛЕЗНЫЕ МОДЕЛИ
class TblPm(models.Model):
    id_pm = models.AutoField(primary_key=True)
    f000 = models.TextField()
    f210 = models.TextField()
    f220 = models.TextField()
    f100 = models.TextField()
    f150 = models.TextField()
    f310 = models.TextField()
    f540 = models.TextField()
    f571 = models.TextField()
    f572 = models.TextField()
    f980 = models.TextField()
    f731 = models.TextField()
    f732 = models.TextField()
    f733 = models.TextField()
    f510 = models.TextField()
    f941 = models.TextField()
    f149 = models.TextField()
    f460 = models.TextField()
    status_pm = models.TextField()

    class Meta:
        db_table = 'tbl_pm'
        managed = True
        verbose_name = 'Полезная модель'
        verbose_name_plural = 'Полезные модели'

    def __str__(self):
        return self.f540


# ПРОМЫЩЛЕННЫЕ ОБРАЗЕЦ
class TblPobr(models.Model):
    id_pobr = models.AutoField(primary_key=True)
    f000 = models.CharField(max_length=20, blank=True, null=True)
    f210 = models.CharField(max_length=20, blank=True, null=True)
    f220 = models.CharField(max_length=30, blank=True, null=True)
    f100 = models.CharField(max_length=20, blank=True, null=True)
    f150 = models.CharField(max_length=30, blank=True, null=True)
    f101 = models.CharField(max_length=10, blank=True, null=True)
    f310 = models.TextField(blank=True, null=True)
    f540 = models.TextField(blank=True, null=True)
    f570 = models.TextField(blank=True, null=True)
    f980 = models.TextField(blank=True, null=True)
    f731 = models.TextField(blank=True, null=True)
    f732 = models.TextField(blank=True, null=True)
    f733 = models.TextField(blank=True, null=True)
    f510 = models.TextField(blank=True, null=True)
    f941 = models.TextField(blank=True, null=True)
    f149 = models.CharField(max_length=30, blank=True, null=True)
    f460 = models.TextField(blank=True, null=True)
    status_po = models.IntegerField()
    link_po = models.CharField(max_length=256)  # Field name made lowercase.

    class Meta:
        db_table = 'tbl_pobr'
        managed = True
        verbose_name = 'Промышленные образец'
        verbose_name_plural = 'Промышленные образцы'

    def __str__(self):
        return self.f540


# РАЦИОНАЛИЗАТОРСКИЕ ПРЕДЛОЖЕНИЯ
class TblRp(models.Model):
    id_rp = models.AutoField(primary_key=True)
    f000 = models.TextField()
    f100 = models.TextField()
    f150 = models.TextField()
    f220 = models.TextField()
    f540 = models.TextField()
    f580 = models.TextField()
    f585 = models.TextField()
    f730 = models.TextField()
    f980 = models.TextField()
    status_rp = models.TextField()

    class Meta:
        db_table = 'tbl_rp'
        managed = True
        verbose_name = 'Рационализаторское предложение'
        verbose_name_plural = 'Рационализаторские предложения'

    def __str__(self):
        return self.f540


# ОБЪЕКТЫ СМЕЖНЫХ ПРАВ
class TblSp(models.Model):
    id_sp = models.AutoField(primary_key=True)
    in_number = models.CharField(max_length=20)
    in_date = models.CharField(max_length=128)
    registration_number = models.CharField(max_length=20)
    name_object = models.CharField(max_length=256)
    publik_place = models.CharField(max_length=256)
    publik_date = models.CharField(max_length=128)
    subject_sp = models.CharField(max_length=256)
    object_name_use = models.CharField(max_length=256)
    object_avtor_use = models.CharField(max_length=256)
    owner_imushest_prav = models.CharField(max_length=256)
    adress_kontact = models.CharField(max_length=256)
    number_svid = models.CharField(max_length=20)
    date_svid = models.CharField(max_length=128)
    iden = models.CharField(max_length=64)
    status_sp = models.IntegerField()

    class Meta:
        db_table = 'tbl_sp'
        managed = True
        verbose_name = 'Объект смежных прав'
        verbose_name_plural = 'Объекты смежных прав'

    def __str__(self):
        return self.name_object


# ТИМС
class TblTims(models.Model):
    id_tims = models.AutoField(primary_key=True, verbose_name='id')
    in_number_t = models.CharField(max_length=128, verbose_name='Входящий номер')
    in_date_t = models.CharField(max_length=128, verbose_name='Дата подачи заявления')
    number_reg_t = models.CharField(max_length=128, verbose_name='Номер заявки')
    app_t = models.CharField(max_length=256, verbose_name='Заявитель')
    owner_t = models.CharField(max_length=256, verbose_name='Правообладатель')
    contact_t = models.CharField(max_length=256, verbose_name='Контактные данные правообладателя')
    name_t = models.CharField(max_length=256, verbose_name='Название ТИМС')
    date_place_t = models.CharField(max_length=128, verbose_name='Дата и место первого выпуска в свет ТИМС')
    avtor_t = models.CharField(max_length=128, verbose_name='Автор')
    referat_t = models.TextField(verbose_name='Аннотация')
    num_svid_t = models.CharField(max_length=128, verbose_name='№ свидетельства')
    date_svid_t = models.CharField(max_length=128, verbose_name='Дата регистрации')
    status_tims = models.IntegerField(verbose_name='Статус')

    class Meta:
        db_table = 'tbl_tims'
        managed = True
        verbose_name = 'ТИМС'
        verbose_name_plural = 'ТИМС'

    def __str__(self):
        return self.name_t


# ТРАДИЦИОННЫЕ ЗНАНИЯ
class TblTrz(models.Model):
    in_trz = models.AutoField(primary_key=True)
    in_number = models.CharField(max_length=20, blank=True, null=True)
    registration_number = models.CharField(max_length=30, blank=True, null=True)
    date_podachi = models.CharField(max_length=30, blank=True, null=True)
    number_svid = models.CharField(max_length=30)
    data_svid = models.CharField(max_length=30)
    zayavitel = models.CharField(max_length=256)
    owner = models.CharField(max_length=256)
    place_of_trz = models.CharField(max_length=256)
    place_trz = models.CharField(max_length=256)
    description_gen = models.CharField(max_length=256)
    nametrz_ru = models.CharField(max_length=256)
    description_ru = models.TextField()
    nametrz_kg = models.CharField(max_length=256)
    description_kg = models.TextField()
    nametrz_en = models.CharField(max_length=256)
    description_en = models.TextField()
    oblast_primeneniya = models.CharField(max_length=256)
    data_end = models.CharField(max_length=30)
    adress_perepiski = models.CharField(max_length=256)
    ssylka = models.CharField(max_length=256)
    coment = models.CharField(max_length=256)
    link_image_trz = models.CharField(max_length=256)
    status_trz = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_trz'
        managed = True
        verbose_name = 'Традиционное знание'
        verbose_name_plural = 'Традиционные знания'

    def __str__(self):
        return self.nametrz_ru

class VidTz(models.Model):
    id_vid_tz = models.AutoField(primary_key=True)
    vid_tz = models.CharField(max_length=128)
    vid_num = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'vid_tz'




