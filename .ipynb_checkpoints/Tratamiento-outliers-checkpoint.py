{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f241399c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def AE_tratamiento_outlier(AE_dataframe, AE_columnas):\n",
    "    AE_parametros_outliers = pd.DataFrame()\n",
    "    for AE_columna in AE_columnas:\n",
    "        AE_quartiles = np.array( AE_dataframe[AE_columna].quantile([.25, .5, .75]) )\n",
    "        AE_irq = AE_quartiles[2] - AE_quartiles[0]\n",
    "        AE_limite_inferior = AE_quartiles[0] - AE_irq*1.5\n",
    "        AE_limite_superior = AE_quartiles[2] + AE_irq*1.5\n",
    "        AE_mean_to = AE_dataframe[AE_columna].mean(axis=0)\n",
    "        AE_median_to = AE_dataframe[AE_columna].median(axis=0)\n",
    "        \n",
    "        AE_parametros_outliers = pd.concat([\n",
    "            AE_parametros_outliers, \n",
    "            pd.DataFrame(data = {\n",
    "                \"columna\": [AE_columna],\n",
    "                \"limite_inferior\": [AE_limite_inferior], \n",
    "                \"limite_superior\": [AE_limite_superior], \n",
    "                \"mean\": [AE_mean_to], \n",
    "                \"median\": [AE_median_to]\n",
    "            })\n",
    "        ], ignore_index=True)\n",
    "        \n",
    "        AE_dataframe.loc[ AE_dataframe[AE_columna] <  AE_limite_inferior, AE_columna ] = AE_mean_to\n",
    "        AE_dataframe.loc[ AE_dataframe[AE_columna] >  AE_limite_superior, AE_columna ] = AE_median_to\n",
    "    return AE_parametros_outliers"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
