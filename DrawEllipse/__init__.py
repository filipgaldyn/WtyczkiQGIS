def classFactory(iface):

    from .drawellipse import DrawEllipse

    """
    Funkcja, która załaduje plugin do QGISa. Importuje ona kod z innego pliku wykonywalnego.
    :param iface: QgisInterface
    :return: DrawEllipse: Klasa, która jest naszą wtyczką
    """
    return DrawEllipse(iface)