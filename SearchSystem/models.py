from django.db import models


#ТОВАРНЫЕ ЗНАКИ
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
    registration_nbr = models.CharField(max_length=256)
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
    id_lic = models.AutoField(primary_key=True, verbose_name='Id')
    id_licen = models.CharField(max_length=20)
    in_date_lic = models.TextField()
    in_number_lic = models.TextField(verbose_name='Номер регистрации ОИС в Кыргызпатенте:')
    date_in_number_lic = models.CharField(max_length=256)
    ois_lic = models.TextField(verbose_name='Наименование ОИС')
    number_lic = models.TextField(verbose_name='Номер регистрации решения')
    date_reg_lic = models.TextField(verbose_name='Дата регистрации')
    name_ois = models.TextField(verbose_name='Название объекта ИС')
    licensiar = models.TextField(verbose_name='Правообладатель / Лицензиар')
    address_licensiar = models.TextField()
    licensiat = models.TextField(verbose_name='Правоприемник / Лицензиат')
    address_licensiat = models.TextField()
    dogovor_lic = models.TextField()
    prava_lic = models.TextField()
    areal_lic = models.TextField()
    date_end_lic = models.TextField(verbose_name='Срок действия договора')
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
    id_avtor = models.AutoField(primary_key=True, verbose_name='Id')
    in_number = models.CharField(max_length=20, verbose_name='Входящий номер')
    in_date = models.CharField(max_length=20, blank=True, null=True, verbose_name='Дата подачи заявки')
    regist_number = models.CharField(max_length=20, verbose_name='Регистрационный номер')
    name_work = models.TextField(verbose_name='Название произведения')
    date_place_public = models.TextField(verbose_name='Дата и место первого обнародования')
    avtor = models.TextField(verbose_name='Автор')
    city_avtor = models.TextField(verbose_name='Страна')
    owner = models.TextField(verbose_name='Обладатель имущественных прав')
    adress_perepiski = models.TextField()
    registration_number = models.CharField(max_length=20, verbose_name='Номер свидетельства о регистрации')
    registration_date = models.TextField(verbose_name='Дата регистрации')
    iden = models.TextField(verbose_name='Идентификатор объекта')
    status_av = models.IntegerField(verbose_name='Статус')
    pseudonym = models.TextField(verbose_name='Псевдоним')
    oap = models.TextField()
    date_av = models.TextField(verbose_name='Дата регистрации свидетельства')
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
    id_bd = models.AutoField(primary_key=True, verbose_name='Id')
    in_number = models.CharField(max_length=20, verbose_name='Входящий номер')
    in_date = models.CharField(max_length=128, verbose_name='Дата подачи заявки')
    number_reg = models.CharField(max_length=20, verbose_name='Регистрационный номер')
    app_b = models.TextField(verbose_name='Заявитель')
    owner = models.TextField(verbose_name='Правообладатель')
    contact = models.CharField(max_length=256, verbose_name='Контакты')
    name = models.TextField(verbose_name='Название БД')
    date_place_bd = models.CharField(max_length=256, verbose_name='Дата и место первого выпуска в свет БД')
    avtor = models.TextField(verbose_name='Автор')
    referat = models.TextField(verbose_name='Аннотация')
    num_svid = models.CharField(max_length=20, verbose_name='Номер свидетельства')
    date_svid = models.CharField(max_length=256, verbose_name='Дата регистрации')
    status_bd = models.IntegerField(verbose_name='Статус')

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
    f000 = models.TextField(verbose_name='Входящий номер')
    f210 = models.TextField(verbose_name='Номер заявки') #номер заявки
    f220 = models.TextField(verbose_name='Дата подачи заявки')
    f100 = models.TextField(verbose_name='Номер охранного документа')
    f150 = models.TextField(verbose_name='Дата регистрации охранного документа')
    f310 = models.TextField(verbose_name='Номер(а)и дата(ы) приоритетной(ых) заявки(ок)')
    f602 = models.TextField()
    f540 = models.TextField(verbose_name='Название') #Название
    f570 = models.TextField()
    f600 = models.TextField(verbose_name='Род, вид (рус)')
    f601 = models.TextField(verbose_name='Род, вид (лат)')
    f980 = models.TextField(verbose_name='Адрес для переписки')
    f731 = models.TextField(verbose_name='Заявитель')
    f732 = models.TextField(verbose_name='Автор')
    f733 = models.TextField(verbose_name='Патентовладелец')
    f941 = models.TextField(verbose_name='Номер журнала и дата прекращения')
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
    id_evm = models.AutoField(primary_key=True, verbose_name='Id')
    in_number = models.CharField(max_length=20, verbose_name='Входящий номер')
    in_date = models.CharField(max_length=128, verbose_name='Дата подачи заявки')
    registration_number = models.CharField(max_length=20, verbose_name='Регистрационный номер')
    app_e = models.CharField(max_length=256, verbose_name='Заявитель')
    owner = models.CharField(max_length=256, verbose_name='Правообладатель')
    adress_kontact = models.CharField(max_length=256, verbose_name='Контакты')
    name_work = models.CharField(max_length=256, verbose_name='Название')
    publik_date_place = models.CharField(max_length=256, verbose_name='Дата и место первого выпуска в свет ЭВМ')
    avtor = models.CharField(max_length=256, verbose_name='Автор')
    referat = models.TextField(verbose_name='Аннотация')
    number_svid = models.CharField(max_length=20, verbose_name='Номер свидетельства')
    date_svid = models.CharField(max_length=128, verbose_name='Дата регистрации')
    status_evm = models.IntegerField(verbose_name='Статус')
    city_owner = models.TextField(verbose_name='Страна')
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
    id_inv = models.AutoField(primary_key=True, verbose_name='Id')
    f000 = models.TextField(blank=True, null=True, verbose_name='Входящий номер')
    f210 = models.TextField(blank=True, null=True, verbose_name='Номер заявки')
    f220 = models.TextField(blank=True, null=True, verbose_name='Дата подачи заявки')
    f100 = models.TextField(blank=True, null=True, verbose_name='Номер охранного документа')
    f101 = models.IntegerField()
    f150 = models.TextField(blank=True, null=True, verbose_name='Дата регистрации охранного документа')
    f310 = models.TextField(blank=True, null=True)
    f540 = models.TextField(blank=True, null=True, verbose_name='Название')
    f571 = models.TextField(blank=True, null=True, verbose_name='Описание')
    f572 = models.TextField(blank=True, null=True)
    f980 = models.TextField(blank=True, null=True, verbose_name='Адрес для переписки')
    f731 = models.TextField(blank=True, null=True, verbose_name='Заявитель')
    f732 = models.TextField(blank=True, null=True, verbose_name='Автор')
    f733 = models.TextField(blank=True, null=True, verbose_name='Патентовладелец')
    f510 = models.TextField(blank=True, null=True, verbose_name='Индекс МПК')
    f941 = models.TextField(verbose_name='Номер журнала и дата прекращения')
    f149 = models.TextField(blank=True, null=True)
    f460 = models.TextField(blank=True, null=True, verbose_name='Дата публикации')
    status_inv = models.IntegerField(verbose_name='Статус')

    class Meta:
        db_table = 'tbl_inv'
        managed = True
        verbose_name = 'Изобретение'
        verbose_name_plural = 'Изобретения'

    def __str__(self):
        return self.f540


#НМПТ
class TblNmpt(models.Model):
    id_nmpt = models.AutoField(primary_key=True, verbose_name='Id')
    in_number = models.CharField(max_length=20, verbose_name='Входящий номер')
    k11 = models.CharField(max_length=20, verbose_name='Номер свидетельства')
    k15 = models.CharField(max_length=256, verbose_name='Дата регистрации')
    k18 = models.CharField(max_length=256, verbose_name='Дата истечения срока дейтсвия')
    k21 = models.CharField(max_length=20, verbose_name='Регистрационный номер')
    k22 = models.CharField(max_length=256, verbose_name='Дата подачи')
    k46 = models.CharField(max_length=256, verbose_name='№/Год публикации')
    k54 = models.CharField(max_length=256, verbose_name='Название')
    vid_tovara = models.TextField(verbose_name='Вид товара')
    k71 = models.CharField(max_length=256, verbose_name='Заявитель')
    k73 = models.TextField(verbose_name='Владелец')
    k57 = models.TextField(verbose_name='Описание')
    k98 = models.TextField(verbose_name='Адрес')
    status_nmpt = models.IntegerField(verbose_name='Статус')
    remark_nmpt = models.TextField(verbose_name='Причина')

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
    k11 = models.CharField(max_length=20, verbose_name='Номер свидетельства')
    k15 = models.CharField(max_length=128, verbose_name='Дата регистрации')
    k54 = models.CharField(max_length=256, verbose_name='Название ОТЗ')
    k73 = models.CharField(max_length=256, verbose_name='Владелец')
    k46 = models.CharField(max_length=128, verbose_name='№/год публикации')
    status_otz = models.IntegerField(verbose_name='Статус')
    app = models.CharField(max_length=64, verbose_name='Дата решения о признании ОТЗ')

    class Meta:
        db_table = 'tbl_otz'
        managed = True
        verbose_name = 'Общеизвестный товарный знак'
        verbose_name_plural = 'Общеизвестные товарные знаки'

    def __str__(self):
        return self.k54


# ПОЛЕЗНЫЕ МОДЕЛИ
class TblPm(models.Model):
    id_pm = models.AutoField(primary_key=True, verbose_name='Id')
    f000 = models.TextField(verbose_name='Входящий номер')
    f210 = models.TextField(verbose_name='Номер заявки')
    f220 = models.TextField(verbose_name='Дата подачи заявки')
    f100 = models.TextField(verbose_name='Номер охранного документа')
    f150 = models.TextField(verbose_name='Дата регистрации охранного документа')
    f310 = models.TextField()
    f540 = models.TextField(verbose_name='Название')
    f571 = models.TextField(verbose_name='Описание')
    f572 = models.TextField()
    f980 = models.TextField(verbose_name='Адрес для переписки')
    f731 = models.TextField(verbose_name='Заявитель')
    f732 = models.TextField(verbose_name='Автор')
    f733 = models.TextField(verbose_name='Патентовладелец')
    f510 = models.TextField(verbose_name='Индекс МПК')
    f941 = models.TextField(verbose_name='Номер журнала и дата прекращения')
    f149 = models.TextField()
    f460 = models.TextField(verbose_name='Дата публикации')
    status_pm = models.TextField(verbose_name='Статус')

    class Meta:
        db_table = 'tbl_pm'
        managed = True
        verbose_name = 'Полезная модель'
        verbose_name_plural = 'Полезные модели'

    def __str__(self):
        return self.f540


# ПРОМЫШЛЕННЫЙ ОБРАЗЕЦ
class TblPobr(models.Model):
    id_pobr = models.AutoField(primary_key=True, verbose_name='Id')
    f000 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Входящий номер')
    f210 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер заявки')
    f220 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Дата подачи заявки')
    f100 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер охранного документа')
    f150 = models.CharField(max_length=30, blank=True, null=True, verbose_name='Дата регистрации охранного документа')
    f101 = models.CharField(max_length=10, blank=True, null=True)
    f310 = models.TextField(blank=True, null=True)
    f540 = models.TextField(blank=True, null=True, verbose_name='Название')
    f570 = models.TextField(blank=True, null=True, verbose_name='Описание')
    f980 = models.TextField(blank=True, null=True, verbose_name='Адрес для переписки')
    f731 = models.TextField(blank=True, null=True, verbose_name='Заявитель')
    f732 = models.TextField(blank=True, null=True, verbose_name='Автор')
    f733 = models.TextField(blank=True, null=True, verbose_name='Патентовладелец')
    f510 = models.TextField(blank=True, null=True, verbose_name=' Индекс МКПО')
    f941 = models.TextField(blank=True, null=True, verbose_name='Номер журнала и дата прекращения')
    f149 = models.CharField(max_length=30, blank=True, null=True)
    f460 = models.TextField(blank=True, null=True, verbose_name='Дата публикации')
    status_po = models.IntegerField(verbose_name='Статус')
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
    id_rp = models.AutoField(primary_key=True, verbose_name='Id')
    f000 = models.TextField(verbose_name='Входящий номер')
    f100 = models.TextField(verbose_name='Номер охранного документа')
    f150 = models.TextField(verbose_name='Дата регистрации охранного документа')
    f220 = models.TextField(verbose_name='Дата подачи заявки')
    f540 = models.TextField(verbose_name='Название')
    f580 = models.TextField(verbose_name='Предприятие, к деятельности которого относится рационализаторское предложение')
    f585 = models.TextField(verbose_name='Предприятие, признавшее рационализаторское предложение')
    f730 = models.TextField(verbose_name='Автор')
    f980 = models.TextField(verbose_name='Адрес для переписки')
    status_rp = models.TextField(verbose_name='Статус')

    class Meta:
        db_table = 'tbl_rp'
        managed = True
        verbose_name = 'Рационализаторское предложение'
        verbose_name_plural = 'Рационализаторские предложения'

    def __str__(self):
        return self.f540


# ОБЪЕКТЫ СМЕЖНЫХ ПРАВ
class TblSp(models.Model):
    id_sp = models.AutoField(primary_key=True, verbose_name='Id')
    in_number = models.CharField(max_length=20, verbose_name='Входящий номер')
    in_date = models.CharField(max_length=128, verbose_name='Дата подачи заявки')
    registration_number = models.CharField(max_length=20, verbose_name='Регистрационный номер')
    name_object = models.CharField(max_length=256, verbose_name='Название ОСП')
    publik_place = models.CharField(max_length=256, verbose_name='Место первого обнародования')
    publik_date = models.CharField(max_length=128, verbose_name='Дата первого обнародования')
    subject_sp = models.CharField(max_length=256, verbose_name='Субъекты смежных прав')
    object_name_use = models.CharField(max_length=256, verbose_name='Название и автор объекта авторского права,'
                                                                    'использованного при создании объекта смежных права')
    object_avtor_use = models.CharField(max_length=256)
    owner_imushest_prav = models.CharField(max_length=256, verbose_name='Обладатель имущественных прав')
    adress_kontact = models.CharField(max_length=256, verbose_name='Контактные данные обладателя имущественных прав')
    number_svid = models.CharField(max_length=20, verbose_name='Номер свидетельства')
    date_svid = models.CharField(max_length=128, verbose_name='Дата регистрации')
    iden = models.CharField(max_length=64, verbose_name='Идентификатор')
    status_sp = models.IntegerField(verbose_name='Статус')

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
    in_trz = models.AutoField(primary_key=True, verbose_name='Id')
    in_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Входящий номер')
    registration_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Номер охранного документа')
    date_podachi = models.CharField(max_length=30, blank=True, null=True, verbose_name='Дата подачи заявки')
    number_svid = models.CharField(max_length=30, verbose_name='Номер свидетельства')
    data_svid = models.CharField(max_length=30, verbose_name='Дата регистрации охранного документа:')
    zayavitel = models.CharField(max_length=256, verbose_name='Заявитель')
    owner = models.CharField(max_length=256, verbose_name='Владелец')
    place_of_trz = models.CharField(max_length=256, verbose_name='Место происхождения')
    place_trz = models.CharField(max_length=256)
    description_gen = models.CharField(max_length=256)
    nametrz_ru = models.CharField(max_length=256, verbose_name='Название(ру)')
    description_ru = models.TextField(verbose_name='Описание(ру)')
    nametrz_kg = models.CharField(max_length=256, verbose_name='Название(кырг)')
    description_kg = models.TextField(verbose_name='Описание(кырг)')
    nametrz_en = models.CharField(max_length=256, verbose_name='Название(англ)')
    description_en = models.TextField(verbose_name='Описание(англ)')
    oblast_primeneniya = models.CharField(max_length=256, verbose_name='Область применения')
    data_end = models.CharField(max_length=30, verbose_name='Дата окончания охранного документа:')
    adress_perepiski = models.CharField(max_length=256, verbose_name='Адрес для переписки:')
    ssylka = models.CharField(max_length=256)
    coment = models.CharField(max_length=256)
    link_image_trz = models.CharField(max_length=256)
    status_trz = models.IntegerField(blank=True, null=True, verbose_name='Статус')

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




