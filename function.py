def get_batch_data(opc_data):
    batch = opc_data['LOTE_AVULSO']
    product_code = opc_data['PRODUTO']
    product_name = cod_to_prod[product_code]
    line = opc_data['LINHA_DE_PRODUCAO']
    position = opc_data['POSICAO']
    cip = opc_data['CIP_USAGE']
    sub_products_codes = all_sub_products_codes[product_name]
    code_conditions = separe_by_comma(sub_products_codes)
    update_where_clause = f"LOTE_AVULSO = ? AND PRODUTO = ? AND LINHA_DE_PRODUCAO = ?"
    batch_product_line = [batch, product_code, line]
    if position == 'MID':
        query = f"""SELECT Caracteristica, Valor, Codigo_de_Material, Lote_de_PA FROM SAP_DATA
                        WHERE Lote_de_Avulso = '{batch}' AND
                        Codigo_de_Material IN ({code_conditions}) AND
                        Caracteristica IN (SELECT Caracteristica FROM SAP_DATA GROUP BY Caracteristica HAVING MAX(Valor) = Valor)"""
        data = db_client.select_query(query)
        has_data = len(data) > 0
        if has_data:
            batch_analyzes = {}
            for row in data:
                aspect, value = row[:2]
                correct_aspect = aspects_key_mapping[aspect]
                if correct_aspect not in batch_analyzes:
                    batch_analyzes[correct_aspect] = value
            sub_product_cod = str(data[0][2])
            sub_product_name = desc_param[sub_product_cod]
            finished_batch = data[0][3]
            batch_data = {
                'batch': batch,
                'product_code': product_code,
                'product_name': product_name,
                'line': line,
                'position': position,
                'sub_product_cod' : sub_product_cod,
                'sub_product_name' : sub_product_name,
                'finished_batch' : finished_batch,
                'cip': cip,
                'batch_analyzes': batch_analyzes
            }
            #update
            db = db_client.get_db()
            cursor = db.cursor()
            batch_analyzes.pop('COR', None)
            batch_analyzes.pop('APARENCIA', None)
            analyzes_found_for_batch = list(batch_analyzes.keys())
            analyzes_values = list(batch_analyzes.values())
            set_columns = ", ".join([f"{column}_FS = ?" for column in analyzes_found_for_batch])
            analyzes_values.extend(batch_product_line)
            update_values = analyzes_values
            update_query = f"""UPDATE OPC_DATA
                                SET STATUS = 'Ready to send', {set_columns}
                                WHERE {update_where_clause}"""
            cursor.execute(update_query, update_values)
            db.commit()
            db.close()
            return batch_data
        else:
            print(f'Não há dados no SAP para este lote. ({batch}-{product_name}-{position}-{line})')
            return
    else:
        columns = ['TEOR_1_AV', 'TEOR_2_AV', 'pH', 'VISCOSIDADE_20S', 'DENSIDADE', 'VISCOSIDADE_100S', 'VISCOSIDADE_75S']
        columns_separated_by_comma = separe_by_comma(columns)
        lims_query = f"""SELECT {columns_separated_by_comma}
                    FROM LIMS_DATA
                    WHERE Batch = '{batch}'
                    AND ProductCode = {product_code}
                    AND DENSIDADE IS NOT NULL
                    AND TEOR_1_AV IS NOT NULL
                    {'AND TEOR_2_AV IS NOT NULL' if product_name != 'Curbix' else ''}"""
        lims_data = db_client.select_query(lims_query)
        has_lims_data = len(lims_data) > 0
        sap_query = f"""SELECT Codigo_de_Material, Lote_de_PA FROM SAP_DATA
                    WHERE Lote_de_Avulso = '{batch}' AND
                    Codigo_de_Material IN ({code_conditions})"""
        sap_data = db_client.select_query(sap_query)
        has_sap_data = len(sap_data) > 0
        if has_lims_data and has_sap_data:
            batch_analyzes = {}
            for i in range(len(columns)):
                column = columns[i]
                batch_analyzes[column] = lims_data[0][i]
            sub_product_cod = str(sap_data[0][0])
            sub_product_name = desc_param[sub_product_cod]
            finished_batch = sap_data[0][1]
        elif has_lims_data is not True:
            print(f'Não há dados no LIMS para este lote. ({batch}-{product_name}-{position}-{line})')
            return
        elif has_sap_data is not True:
            print(f'Não há dados no SAP para este lote. ({batch}-{product_name}-{position}-{line})')
            return
        batch_data = {
            'batch': batch,
            'product_code': product_code,
            'product_name': product_name,
            'line': line,
            'position': position,
            'sub_product_cod' : sub_product_cod,
            'sub_product_name' : sub_product_name,
            'finished_batch' : finished_batch,
            'batch_analyzes': batch_analyzes
        }
        #update
        db = db_client.get_db()
        cursor = db.cursor()
        analyzes_found_for_batch = list(batch_analyzes.keys())
        analyzes_values = list(batch_analyzes.values())
        set_columns = ", ".join([f"{column}_FS = ?" for column in analyzes_found_for_batch if column != 'COR' and column != 'APARENCIA'])
        analyzes_values.extend(batch_product_line)
        update_values = analyzes_values
        update_query = f"""UPDATE OPC_DATA
                            SET STATUS = 'Ready to send', {set_columns}
                            WHERE {update_where_clause}"""
        cursor.execute(update_query, update_values)
        db.commit()
        db.close()
        return batch_data
