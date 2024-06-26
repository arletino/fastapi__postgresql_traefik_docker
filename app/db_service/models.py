from sqlmodel import Field, SQLModel 


class Part(SQLModel, table=True):
    ''' Class table spare_parts '''
    __tablename__ = 'spare_parts'
    
    id: int | None = Field(default=None, primary_key=True)
    article: str | None = None
    article_unit: str | None = None
    serial_number_machine: str | None = None
    alternative_article: str | None = None
    name_eng: str | None = None
    name_ru: str | None = None
    material: str | None = None
    weight_kg: str | None = None
    size: str | None = None
    part_type: str | None = None
    description_custom: str | None = None
    manufacturer: str | None = None
    trade_mark: str | None = None
    qty_in_unit: str | None = None
    country_eng: str | None = None
    s_code: str | None = None
    path_catalog: str | None = None
    path_documentation: str | None = None
    path_photo: str | None = None
    path_avatar: str | None = None
    hashtags: str | None = None
    createAt: str | None = None
    changeAt: str | None = None
    comment: str | None = None

class Installed_machine(SQLModel, table=True):
   '''Class table installed machines''' 
    __tablename__ = 'installed_machines'
    
    machine_id: int | None = Field(default = None, primary_key=True)
    machine_sn: str | None
    name_short: str | None
    name_full: str | None
    custmer_id: int | None
    installation_date: str | None
    installation_city_ru: str | None
    installation_city_eng: str | None
    installation_adress: str | None
    path_documentation: str | None
    machine_status: str | None
    machine_type: str | None
    createAt: str | None
    changeAt: str | None
    comment: str | None

class Customer(SQLModel, table=True):
    '''Class table customer'''
    __tablename__ = 'customers'
    cust_id: int | None = Field(default = None, primary_key=True)
    customet_id: str | None
    customer_name_ru: str | None
    customer_name_en: str | None
    company_type: str | None
    region_ru: str | None
    region_en: str | None
    createAt: str | None
    changeAt: str | None
    comment: str | None

class Customer_contact(SQLModel, table=True):
    '''Class table customer'''
    __tablename__ = 'customer_contacts'
    customer_contact_id str | None = Field(default = None, primary_key=True)

