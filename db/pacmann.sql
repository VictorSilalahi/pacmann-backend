PGDMP     /        
            {         	   pacmanndb    13.5    13.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    66444 	   pacmanndb    DATABASE     i   CREATE DATABASE pacmanndb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_Indonesia.1252';
    DROP DATABASE pacmanndb;
                pacmann    false            �            1259    66465    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    pacmann    false            �            1259    66448    ttodos    TABLE       CREATE TABLE public.ttodos (
    todoid integer NOT NULL,
    title character varying(50),
    "desc" character varying(200),
    status character varying(10),
    userid integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
    DROP TABLE public.ttodos;
       public         heap    pacmann    false            �            1259    66446    ttodos_todoid_seq    SEQUENCE     �   CREATE SEQUENCE public.ttodos_todoid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.ttodos_todoid_seq;
       public          pacmann    false    201            �           0    0    ttodos_todoid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.ttodos_todoid_seq OWNED BY public.ttodos.todoid;
          public          pacmann    false    200            �            1259    66456    tusers    TABLE       CREATE TABLE public.tusers (
    userid integer NOT NULL,
    username character varying(30),
    email character varying(30),
    pwd character varying(200),
    imgpath character varying(500),
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
    DROP TABLE public.tusers;
       public         heap    pacmann    false            �            1259    66454    tusers_userid_seq    SEQUENCE     �   CREATE SEQUENCE public.tusers_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.tusers_userid_seq;
       public          pacmann    false    203            �           0    0    tusers_userid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.tusers_userid_seq OWNED BY public.tusers.userid;
          public          pacmann    false    202            .           2604    66451    ttodos todoid    DEFAULT     n   ALTER TABLE ONLY public.ttodos ALTER COLUMN todoid SET DEFAULT nextval('public.ttodos_todoid_seq'::regclass);
 <   ALTER TABLE public.ttodos ALTER COLUMN todoid DROP DEFAULT;
       public          pacmann    false    200    201    201            /           2604    66459    tusers userid    DEFAULT     n   ALTER TABLE ONLY public.tusers ALTER COLUMN userid SET DEFAULT nextval('public.tusers_userid_seq'::regclass);
 <   ALTER TABLE public.tusers ALTER COLUMN userid DROP DEFAULT;
       public          pacmann    false    203    202    203            �          0    66465    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          pacmann    false    204   W       �          0    66448    ttodos 
   TABLE DATA           _   COPY public.ttodos (todoid, title, "desc", status, userid, created_at, updated_at) FROM stdin;
    public          pacmann    false    201   �       �          0    66456    tusers 
   TABLE DATA           _   COPY public.tusers (userid, username, email, pwd, imgpath, created_at, updated_at) FROM stdin;
    public          pacmann    false    203   T       �           0    0    ttodos_todoid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.ttodos_todoid_seq', 16, true);
          public          pacmann    false    200            �           0    0    tusers_userid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.tusers_userid_seq', 11, true);
          public          pacmann    false    202            5           2606    66469 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            pacmann    false    204            1           2606    66453    ttodos ttodos_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.ttodos
    ADD CONSTRAINT ttodos_pkey PRIMARY KEY (todoid);
 <   ALTER TABLE ONLY public.ttodos DROP CONSTRAINT ttodos_pkey;
       public            pacmann    false    201            3           2606    66464    tusers tusers_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.tusers
    ADD CONSTRAINT tusers_pkey PRIMARY KEY (userid);
 <   ALTER TABLE ONLY public.tusers DROP CONSTRAINT tusers_pkey;
       public            pacmann    false    203            �           826    66445    DEFAULT PRIVILEGES FOR TABLES    DEFAULT ACL     ^   ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES  TO pacmann WITH GRANT OPTION;
                   postgres    false            �      x�KI3751I���0H����� ,2�      �   �   x�u��� �gx
_@s�	V�N:ut�Ɛh�&<~��QL�;����nS3�	 ����߃��ƚ�)V�������5�զ��K �T��C�}�@	�f���Q[�nb�Vr{-�I��F�տ�) � 8w�/�c�|�#�&����*�tdi�
�B��H������Ha����8���#��x�)�"����B�:�&B�0      �   �  x����nG��WO����A�s�US92\v�$��glY���N��E,@-���X`���5���r��?]����(��CZi5��7b�������|<��n������55c��%�'���*�:T��jȞ(���BIR����gDݧa���|��nӲ��2�/>_�oN��9U?�z	�YM���R�d�JJ�T)�E9I96�F��(�q�5��f�v�H^���v��ٹ�e]�8��q<�n�}n.Jp�k�LB��k(�̈́�d��b0 �����=yn�o��.*�fѥ/'?_�MV8�[U��u��I%W*rY�"�4�dLh�H�o�4VΒi`ޔ]�Zֺ��C������?�����򷾂�ƒkbl�j5pmj���$���(`�Mo��}���}�����p��ޫ۳�Oi�E)�����⶟��RStѓz�B�Qs�F�|�d� �&���>;_ֲ7y�[��.�����ǫKX^>��L��ì�9��� !���=Vp;ى�9�$Wۭ*h�����A*d�x#t7uyz�o١��t�o&/�_�=��I��iڢmդ���rlC�%r�Ί�d3����;߆�Q�R������r3���i��e�z��\�S�F��&���J�MP�ILV�*x�J�,E	��Q'Զ� ҏ�0��{4���9f>2��*������h4� }V:     