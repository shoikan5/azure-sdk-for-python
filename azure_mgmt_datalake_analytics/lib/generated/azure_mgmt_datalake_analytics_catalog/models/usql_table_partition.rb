# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::DataLakeAnalytics::Catalog
  module Models
    #
    # A Data Lake Analytics catalog U-SQL table partition item.
    #
    class USqlTablePartition < CatalogItem

      include MsRestAzure

      # @return [String] the name of the database.
      attr_accessor :database_name

      # @return [String] the name of the schema associated with this table
      # partition and database.
      attr_accessor :schema_name

      # @return [String] the name of the table partition.
      attr_accessor :name

      # @return [DdlName] the Ddl object of the partition's parent.
      attr_accessor :parent_name

      # @return [Integer] the index ID for this partition.
      attr_accessor :index_id

      # @return [Array<String>] the list of labels associated with this
      # partition.
      attr_accessor :label

      # @return [DateTime] the creation time of the partition
      attr_accessor :create_date


      #
      # Mapper for USqlTablePartition class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'USqlTablePartition',
          type: {
            name: 'Composite',
            class_name: 'USqlTablePartition',
            model_properties: {
              compute_account_name: {
                required: false,
                serialized_name: 'computeAccountName',
                type: {
                  name: 'String'
                }
              },
              version: {
                required: false,
                serialized_name: 'version',
                type: {
                  name: 'String'
                }
              },
              database_name: {
                required: false,
                serialized_name: 'databaseName',
                type: {
                  name: 'String'
                }
              },
              schema_name: {
                required: false,
                serialized_name: 'schemaName',
                type: {
                  name: 'String'
                }
              },
              name: {
                required: false,
                serialized_name: 'partitionName',
                type: {
                  name: 'String'
                }
              },
              parent_name: {
                required: false,
                serialized_name: 'parentName',
                type: {
                  name: 'Composite',
                  class_name: 'DdlName'
                }
              },
              index_id: {
                required: false,
                serialized_name: 'indexId',
                type: {
                  name: 'Number'
                }
              },
              label: {
                required: false,
                serialized_name: 'label',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'StringElementType',
                      type: {
                        name: 'String'
                      }
                  }
                }
              },
              create_date: {
                required: false,
                serialized_name: 'createDate',
                type: {
                  name: 'DateTime'
                }
              }
            }
          }
        }
      end
    end
  end
end